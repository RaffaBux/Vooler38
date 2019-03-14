from threading import Thread
import socket
def run(serversocket,bufferdati,pas,risposta,clientsocket,controllo):
	client_soc,indirizzo=serversocket.accept()
	controllo="avanti"
	while risposta=="sbagliata":
		client_soc.send((''.join(pas)).encode())
		dati=client_soc.recv(bufferdati).decode()
		pas=dati
		clientsocket.send((''.join(pas)).encode())
		risposta=clientsocket.recv(bufferdati).decode()
	client_soc.close()
bufferdati=1024
clientsocket=socket.socket()
clientsocket.connect(('localhost',8081))
n=clientsocket.recv(bufferdati).decode()
lunghezza=int(n)
pas=list()
print(lunghezza)
for i in range(0,lunghezza):
	pas.append("a")
clientsocket.send((''.join(pas)).encode())
print(''.join(pas))
risposta=clientsocket.recv(bufferdati).decode()
print(risposta)
if risposta=="sbagliata":
	serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	serversocket.bind(('localhost',4444))
	serversocket.listen(lunghezza)
	controllo="stop"
	while risposta=="sbagliata":
		try:
       			Thread(target=run, args=(serversocket, bufferdati,pas,risposta,clientsocket,controllo)).start()
		except:
			print("Thread did not start.")
			traceback.print_exc()
		while controllo=="stop":
			pass
clientsocket.close()	




				
