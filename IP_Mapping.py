#IP Mapping

import socket

name = socket.gethostname()
ip = socket.gethostbyname(name)

print ("The IP address of target is: ", ip)
