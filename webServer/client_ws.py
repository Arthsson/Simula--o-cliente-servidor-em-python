import socket

HOST = "localhost"
PORT = 40000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))
print('deu certo ')


arq = open("Leitura.txt", "r")

for i in arq.readlines():
    print(i,'\n')
    s.send(i.encode())
    
arq.close()
s.close()



