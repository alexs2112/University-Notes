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
