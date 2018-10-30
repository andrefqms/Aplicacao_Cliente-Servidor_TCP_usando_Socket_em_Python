# coding: utf-8
import socket

# Terminal HOST: ifconfig
# PORT aleatoria acima de 1024
HOST = raw_input()  # Endereco IP do Servidor
PORT = raw_input()	# Porta que o Servidor esta

# Atribui uma Conexao TCP
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
print 'Para sair use CTRL+C\n'

# Ler entrada do cliente
msg = raw_input()

#Enquanto mensagem for  diferente de 'bye', retorna a própria entrada
while msg != 'bye':
    tcp.send (msg)
    saida = tcp.recv(1024)
    print saida
    msg = raw_input()
tcp.close()
