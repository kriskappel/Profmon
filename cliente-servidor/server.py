import socket
import thread
import threading


def conectado(con, cliente):
	print '\nConectado por', cliente

	while True:
		msg = con.recv(1024)
		if(len(msg) != 0):
			print (cliente, msg)
			con.sendall('CONNECTED')


	print '\nFinalizando conexao do cliente', cliente
	con.close()
	thread.exit()


HOST = ''  # Endereco IP do Servidor
PORT = 5000  # Porta que o Servidor esta
numeroClientes = 2
numeroClientesCadastrados = 0
threadsClientes = [None]*numeroClientes

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
# Colocando um endereco IP e uma porta no Socket
tcp.bind(orig)
# Colocando o Socket em modo passivo para receber dois clientes
tcp.listen(2)



print'\nServidor TCP concorrente iniciado no IP', HOST, 'na porta', PORT, '\n\n'
while True:
    # Aceitando uma nova conexao

	if numeroClientesCadastrados == numeroClientes:
		print 'Numero de usuarios maximos alcancados'

	while True:
		con, cliente = tcp.accept()
		thread.start_new_thread(conectado, tuple([con, cliente]))

	numeroClientesCadastrados += 1

# Fechando a conexao com o Socket
tcp.close