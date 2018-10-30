# coding: utf-8
import socket

# Terminal HOST: ifconfig
# PORT aleatoria acima de 1024
HOST = raw_input()  # Endereco IP do Servidor
PORT = raw_input()	 # Porta que o Servidor esta

# Atribuindo uma Conexao TCP
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Se fechar inesperadamente, a Conexao é fechada
tcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Atribuindo uma Conexao TCP
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)

while True:
	# Estabelece "ID" de uma Conexao TCP/Cliente (con)
    con, cliente = tcp.accept()
    # Recebendo mensagem do cliente e retorna a mesma para ele
    while True:
        msg = con.recv(1024)
        con.send(msg)
        if not msg: break
    print 'Finalizando conexao do cliente', cliente    
    con.close()
