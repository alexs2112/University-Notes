 - Writing a botnet, network of computers gathered by an attacker that can connect to a single central command center
 - Final two tasks are only worth 20% of the assignment but will take 80% of the time (IRC tasks)

`nc --broker -l <port>`
 - Opens a server that accepts multiple connections on port

`nc <server> <port>`
 - Connect to the server
 - Writing anything on this connection will propagate it to all other connections (but not the server)
 - I think our `nccontroller` is a connection to the netcat server, the `ncbot`s are also connections
