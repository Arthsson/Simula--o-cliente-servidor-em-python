import socket

HOST = '127.0.0.1'
PORT = 11000 

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = input("Mensagem a ser enviada: ")
client.sendto(str.encode(message), (HOST,PORT))

client.close()
