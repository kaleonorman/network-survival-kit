import socket

domain = input('Please input the domain name: ') 	
ip = socket.gethostbyname(domain)
print (ip)

start = input('Scan from range: ')
finish = input('To range: ')		
	
for x in range(int(start),int(finish)):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	con = s.connect_ex((ip,x))
	if con == 0:
		print("Port", x, ": OPEN")

s.close()
