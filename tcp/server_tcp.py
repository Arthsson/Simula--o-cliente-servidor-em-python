import socket

HOST = 'localhost'
PORT = 10000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST,PORT))
server.listen()
print("Aguardando...")
conection, addrees = server.accept()

print("Conectado em {}".format(addrees))

#troca de msg 
while True:
    data = conection.recv(2048) 
    if not data: 
        print("Encerrando Conexão...")
        conection.close()
        break
    conection.sendall(data) 