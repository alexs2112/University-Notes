 - Writing a botnet, network of computers gathered by an attacker that can connect to a single central command center
 - Final two tasks are only worth 20% of the assignment but will take 80% of the time (IRC tasks)

`nc --broker -l <port>`
 - Opens a server that accepts multiple connections on port

`nc <server> <port>`
 - Connect to the server
 - Writing anything on this connection will propagate it to all other connections (but not the server)
 - I think our `nccontroller` is a connection to the netcat server, the `ncbot`s are also connections

For the controller
 - Use a non-blocking socket, or
 - Use python `select`, it can take a timeout (best option)
	 - Suspend the execution until one of the sockets can be read from, the other socket can be written to
	 - Wait for a timeout until this has been done
	 - I think the input param (first one) is a list of sockets that you want to read from, the output param (second) is a list of outputs to write to
 - Wait for data to be sent through the socket

Use port forwarding on assignment so you can setup an SSH tunnel to talk between the IRC bots