import socket
import thread
import threading
import time

clients = []
clients_lock = threading.Lock()

key = None

character_list = []
points_list = []
atack = []
file = open("entrada.txt","r")


for item in file:
	line = item.split(",")
	character_list.append(line[0])
	points_list.append([int(line[1]), int(line[2]), int(line[3])])
	atack.append([line[4],line[5][:-1]])

def conectado(con, cliente, numClientes):
	print '\nConectado por', cliente
	enemy_player = 0
	global key


	while True:
		msg= con.recv(4096)

		if(len(msg) != 0):
			print (cliente, msg, numClientes)
			
			break

	#Quando player 1 conecta
	if(numClientes == 0):
		
		con.sendall('CONNECTED. Waiting for Player 2')
		
		ts = con.recv(4096)
		with clients_lock:
			key = ts


		while True:
			msg = con.recv(1024)
			if(msg == 'waiting'):

				with clients_lock:
					enemy_player = clients[1]
				
				break
			
	#Quando o player 2 conecta
	elif(numClientes == 1):
		
		with clients_lock:
			enemy_player = clients[0]
		
		enemy_player.sendall('PLAYER 2 CONNECTED')
		con.sendall('CONNECTED \nPLAYER 1 BANNING')
		
		with clients_lock:
			print key
			con.sendall(key)

	send_lists(con)


	while True:
		msg = con.recv(1024)

		print (cliente, msg, numClientes)
		enemy_player.sendall(msg)

		# if(len(msg) != 0):

		# 	con.sendall('CONNECTED')


	print '\nFinalizando conexao do cliente', cliente
	con.close()
	thread.exit()

def send_lists(tcp):
	with open ("entrada.txt", "r") as myfile:
		data = myfile.read()
		tcp.sendall(data)
	# for i in range (0,8):
	# 	data = character_list[i]
	# 	tcp.sendall(data)

	# for i in range (0,8):
	# 	data = str(points_list[i][0])
	# 	tcp.sendall(data)
	# 	data = str(points_list[i][1])
	# 	tcp.sendall(data)
	# 	data = str(points_list[i][2])
	# 	tcp.sendall(data)	

	# for i in range (0,8):
	# 	data = atack[i][0]
	# 	tcp.sendall(data)
	# 	data = atack[i][1]
	# 	tcp.sendall(data)
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

		with clients_lock:
			clients.append(con)

		#print numeroClientesCadastrados
		thread.start_new_thread(conectado, tuple([con, cliente, numeroClientesCadastrados]))
		numeroClientesCadastrados += 1

# Fechando a conexao com o Socket
tcp.close