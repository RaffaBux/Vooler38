import socket
password=input("Inserisci una password: ")
print(len(password))
serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serversocket.bind(('localhost',8081))
serversocket.listen(2)
bufferdati=1024
client_soc,indirizzo=serversocket.accept()
while True:
	client_soc.send(str(len(password)).encode())
	dati=client_soc.recv(bufferdati).decode()
	''.join(dati)
	print(dati)
	if dati==password:
		client_soc.send("corretta".encode())
		break
	else:
		client_soc.send("sbagliata".encode())
client_soc.close()
