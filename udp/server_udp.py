import socket

HOST = 'localhost'
PORT = 11000

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST,PORT))


print("Aguardando a conexão...")
message_received, addrees_client = server.recvfrom(2048) # dados recebidos serão colocados nessas duas variaveis 
print("Menssagem recebida {} {}".format(message_received,addrees_client))

server.close()
