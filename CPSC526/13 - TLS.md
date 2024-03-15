### Transport Layer Security (TLS)
 - Cryptographic protocol for secure end-to-end communication
	 - Nearly all of internet today runs on top of SSL/TLS
	 - Typical example: HTTPS over TLS = HTTPS
 - TLS provides:
	 - Authentication, forward security - via public-key crypto and certificates
	 - Confidentiality - via symmetric-key encryption
	 - Integrity - via GCM or MAC
	 - Prevents MITM, injection, replay attacks, impersonation, ...
 - TLS evolved from older protocol, called SSL (Secure Socket Layer)
 - Enabled between HTTP and the TCP connection

**Use Case**:
 - Imagine you want to check your email
	 - At a public cafe
	 - Where the router is hacked
	 - And it goes through an evil ISP
	 - And you're in a country that wants to spy on you
 - Does TLS or HTTPS protect you?
 - Yes, but
	 - Provided no malware is on your computer
	 - All installed root CAs are trustworthy
	 - You do not ignore browser warnings about bad certificates
	 - Someone could still detect which/whether/when websites you are contacting
		 - To hide this, you need something like VPN, TOR, SSH Tunnel

**SSL/TLS in Code**:
 - Bad news: SSL/TLS protocol is quite complicated (RFC8446)
 - Good news: Free implementations exist for just about every language & OS
	 - Designed to be "easily" added to existing code
```python
import socket, ssl, pprint
from urllib.parse import urlparse

url="https://gitlab.com/cpsc526w24/a3-dekrypt/-/raw/main/README.md?ref_type=heads"
purl = urlparse(url)
context = ssl.create_default_context()
with socket.create_connection((purl.hostname, 443)) as sock:
  with context.wrap_socket(sock, server_hostname=purl.hostname) as ssock:
    req = (
        f"GET {purl.path} HTTP/1.0\r\n"
        f"Host: {purl.hostname}\r\n"
        f"\r\n"        
    )
    ssock.sendall(req.encode())
    reply = b""
    while blk := ssock.recv(1024):
      reply += blk
    pprint.pprint(reply.split(b"\r\n"))
```

**SSL/TLS: History**:
 - SSL 1.0-3.0 by Netscape (1994-1996)
 - TLS 1.0 based on SSL 3.0, released in 1999, RFC2246
	 - Small but important differences, not compatible
 - TLS 1.1 in 2006
	 - Some major changes (fixes to CBC modes)
 - TLS 1.2 in 2008
	 - More major changes (added AES, replaced MD5 with SHA256)
 - TLS 1.3 in 2018 (current)
	 - Removed many weak crypto schemes, added new strong ones
	 - Performance improvements
	 - Scrutinized since 2015

**TLS in Network Stack**:
 - Can provide security to any application that uses TCP
 - Since TLS lives above the OS level, it does not require OS support
 - API similar to typical socket interface, so it is easy to add security to an app

**TLS: Two Primary Components**:
  - Handshake Protocol
	  - Authentication of parties
	  - Negotiation of crypto algorithms and related parameters
	  - Establishment of shared secret key
	  - Uses public-key crypto, signatures, certificates
  - Record Protocol
	  - Applications talk securely using parameters established during handshake
	  - Uses symmetric cryptography and message authentication

**Handshake Protocol (Typical)**:
 - client -> server: "ClientHello"
	 - Browser includes list of supported cipher suites, ordered by preference
		 - `TLS_AES_256_GCM_SHA384`, etc
	 - Browser includes some random bytes for DHKE & PFS
 - server -> client: "ServerHello"
	 - Server picks and sends the best cipher suite with some random bytes
	 - Server includes its certificate
	 - Server proves to client it has matching private key by signing all messages with it
 - client -> server
	 - Browser verifies server's certificate
	 - Optionally, client can send its certificate as well
	 - Browser computes MAC of all messages so far and sends it to server
 - If server can verify the MAC, both can start communicating using symmetric cipher

**TLS Connection Between (C)lient and (S)erver**:
![[tls_handshake_protocol.png|500]]

**DHKE in TLS**:
![[DHKE_TLS_0.png|400]]
 - Both compute shared secret `g^(ab) mod p` and use it to derive (using HKDF) various secrets, such as IV, MAC secrets, AES session keys
![[DHKE_TLS_1.png|400]]
 - All subsequent messages are encrypted with the negotiated cipher and key derived from shared secret
 - All messages are sequentially numbered to prevent replay attacks

**Using OpenSSL to Inspect TLS Handshake**:
`$ openssl s_client -verify_quiet -trace -tls1_3 www.cloudflare.com:443`
 - Generates a ton of output

**DTLS: Datagram TLS**:
 - A UDP-based variant of TLS
 - Not as widely used, but still standardized
 - Provides the security of TLS without needing guarantees of TCP

**TLS Downgrade Attack**:
 - TLS allows communication between newer versions and older versions
	 - Backward compatibility is often a source of vulnerabilities
 - MITM could downgrade TLS version to expose weaker/vulnerable ciphers
	 - eg. Alice and Bob both understand TLS 1.3, but Eve could convince them to downgrade to 1.1
 - TLS 1.3 protects against downgrade attack
	 - If either side supports TLS 1.3, it is impossible to downgrade to earlier versions
 - But you could be browsing a site using older TLS versions

**SSL Stripping Attack**:
 - When you go to a website without explicitly stating `https`, the browser might attempt to connect to the `http` version
 - The site you want to go to will likely send a reply with the `http` redirect to `https`
 - MITM could intercept the redirect
	 - Alice -> sends HTTP requests -> Eve -> rewrites as HTTPS requests -> Bob
	 - Bob -> returns HTTPS replies  -> Eve -> strips "https" from any links -> Alice

**HSTS**:
 - Simple mechanism to ensure users always connect to a website using `https://`
 - On first visit, website tells browser it has enabled HSTS by returning an HTTP header
   `String-Transport-Security: max-age=3156000;`
 - Easily configured in most popular web servers
 - Browser remembers this, next time user types the same website address, the browser will automatically connect using `https://`
 - Even better, sign up your website for https://hstspreload.org
