import socket
import _thread
import threading


def conectado(con, cliente):
	print ('Conectado por', cliente)

	while True:
		msg = con.recv(1024)
		if not msg: break
		print (cliente, msg)

	print ('Finalizando conexao do cliente', cliente)
	con.close()
	_thread.exit()


HOST = ''  # Endereco IP do Servidor
PORT = 5000  # Porta que o Servidor está
numeroClientes = 2
numeroClientesCadastrados = 0
threadsClientes = [None]*numeroClientes

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
# Colocando um endereço IP e uma porta no Socket
tcp.bind(orig)
# Colocando o Socket em modo passivo para receber dois clientes
tcp.listen(2)

print('\nServidor TCP concorrente iniciado no IP', HOST, 'na porta', PORT)
while True:
    # Aceitando uma nova conexão

	if numeroClientesCadastrados == numeroClientes:
		print('Número de usuários máximos alcançados')

	while True:
		con, cliente = tcp.accept()
		_thread.start_new_thread(conectado, tuple([con, cliente]))

	numeroClientesCadastrados += 1

# Fechando a conexão com o Socket
tcp.close