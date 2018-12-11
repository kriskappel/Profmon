import socket
#import player
import sys



character_list = ["Marilton", "Paulo", "Torchelsen", "Pilla", "Leomar", "Luciana", "Simone", "Rafa", "Tati", "Guilherme", "Porto", "Lisane", "Felipe", "Substituto", "Cesar Menotti", "Du Bois", "Renata", "Gerson", "Ferrugem", "Ana"]

def initial_print():
	print "================================================================"
	print "========================WELCOME TO PROFMON======================"
	print "================================================================"
	print "."
	print "."
	print "."
	print "CONNECTING"
	print "."
	print "."
	print "."

def server_connect():

	HOST = '192.168.0.34'   # Endereco IP do Servidor
	PORT = 5000  # Porta que o Servidor esta

	server = (HOST, PORT)
	# Criando a conexao
	tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	tcp.connect(server)

	mensagem_inicio_conexao = 'Mensagem recebida'
	tcp.send(mensagem_inicio_conexao.encode())

	while True:
		data = tcp.recv(1024)
		if(len(data) != 0):
			print "Received response: " + str(data)
			break

	return tcp


	#conexao(me, server)
def test_connection(tcp):
	while True:
		test_input = input("press 1\n")
		while (test_input != 1):
			test_input = input("press 1\n")
		test_input = 0
		#-------------- Iniciando a conexao com o servidor -------------
		mensagem_inicio_conexao = 'Mensagem recebida'
		tcp.send(mensagem_inicio_conexao.encode())

		while True:
			data = tcp.recv(1024)
			if(len(data) != 0):
				print "Received response: " + str(data)
				break

def send_msg(tcp, msg):
	#mensagem_inicio_conexao = 'Mensagem recebida'
	tcp.send(msg)

	while True:
		data = tcp.recv(1024)
		if(len(data) != 0):
			print_banned(int(msg))
			break
	
# def conexao(me, server):
# 	HOST = ''  # Endereco IP do Servidor
# 	PORT = 5001  # Porta que o Servidor esta
# 	tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 	orig = (HOST, PORT)
# 	tcp.bind(orig)
# 	tcp.listen(1)
# 	con, cliente = tcp.accept()

	
	# while True:
	# 	msg = con.recv(1024)
	# 	if not msg: break
	# 	print (cliente, msg)


def ban(tcp):
	print "===SELECT CHARACTER TO BE BANNED==="
	print_chars([])
	print ""
	banned = input("")

	send_msg(tcp, str(banned - 1))

	return (banned - 1)

def print_banned(number):
	print character_list[number] + " BANNED!"

def print_chars(unavailable):
	unavailable = unavailable
	for i in range(0, len(character_list)):
		if((i + 1) not in unavailable):
			print str(i + 1) + " " + character_list[i]

# def pick_char(banlist):
# 	unavailable = banlist
# 	print "\n===SELECT CHARACTER TO BE PICKED==="
# 	print_chars(unavailable)
# 	print ""
# 	id_pick = input("")
# 	print "\n" + character_list[id_pick - 1] + " PICKED"
# 	return id_pick




if __name__ == "__main__":
	
	banlist = []
	my_team = player.Player(3)
	enemy_team = player.Player(3)

	tcp = 0

	initial_print()

	#conexao(me, server)
	tcp = server_connect()
	
	#test_connection(tcp)

	banned = ban(tcp)

	banlist.append(banned)

	#send_msg(tcp)


	# while (sys.stdin.read(1) != "\n"):
	# 	pass
	# banlist = []
	# player1 = player.Player(3)
	# player2 = player.Player(3)

	# banlist.append(ban())

	# for i in range(0, 2):
	# 	p1char = pick_char(banlist)
	# 	player1.add_char(p1char)
	# 	banlist.append(p1char)

	# 	p2char = pick_char(banlist)
	# 	player2.add_char(p2char)
	# 	banlist.append(p2char)

	# print ""
	# player1.printTeam()
	# player2.printTeam()
	# print "======="
