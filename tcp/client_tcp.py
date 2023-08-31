import socket

HOST = 'localhost' 
PORT = 10000 

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))  

client.sendall(str.encode("Mensagem do cliente\n"))
data = client.recv(2048)

print("A mensagem foi enviada\n",data.decode())

client.close()