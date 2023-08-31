import socket

HOST = ''
PORT = 40000
print('servidor Iniciando  ')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)

conn, addr = s.accept()

arq = open('SLeitura.txt', 'wb')

while 1:
    dados = conn.recv(8)
    if not dados:
        break
    arq.write(dados)
arq.close()
conn.close()
print('servidor Encerrado')