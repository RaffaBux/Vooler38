import socket
clientsocket=socket.socket()
hostname='localhost'
portasocket=4444
bufferdati=1024
clientsocket.connect((hostname,portasocket))
while True:
	print("gesu")
	datiricevuti=clientsocket.recv(bufferdati).decode()
	a=datiricevuti.list()
	lun=len(datiricevuti)
	for i in range(0,lun):
		if datiricevuti[lun-1-i]!='z':
			datiricevuti[lun-1-i]=chr(ord(datiricevuti[lun-1-i])+1)
			break
	clientsocket.send(datiricevuti.encode())
clientsocket.close()


