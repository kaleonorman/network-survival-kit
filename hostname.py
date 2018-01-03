import socket
# This function displays the hostname of the PC.

def host():
	name = socket.gethostname()

	print ("The hostname is: ", name)

if __name__ == '__main__':
	host()


