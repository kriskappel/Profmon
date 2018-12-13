import socket
import player
import sys
import time

#character_list = ["Marilton", "Paulo", "Torchelsen", "Pilla", "Leomar", "Luciana", "Simone", "Rafa", "Tati", "Guilherme", "Porto", "Lisane"]
character_list = []
points_list = []
atack = []
key = 0


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

	HOST = '192.168.90.37'   # Endereco IP do Servidor
	PORT = 5000  # Porta que o Servidor esta

	player = 0

	server = (HOST, PORT)
	# Criando a conexao
	tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	tcp.connect(server)

	mensagem_inicio_conexao = 'Mensagem recebida'
	tcp.send(mensagem_inicio_conexao)


	while True:
		data = recv_msg(tcp, 1024)

		flag = False
		#PARTE PLAYER 1
		if(data == 'CONNECTED. Waiting for Player 2'):
			player = 1
			print str(data)

			#ts = str(time.time())
			#tcp.send(ts)
			#key = ts
			##print key

			while True:
				data = recv_msg(tcp, 1024)
				if(data == 'PLAYER 2 CONNECTED'):
					print data
					tcp.send('waiting')
					flag = True
					break
			if flag == True:
				break	

		#PARTE PLAYER 2
		elif(data == 'CONNECTED \nPLAYER 1 BANNING'):
			player = 2
			print str(data)

			#key = recv_msg(tcp, 1024)
			#print key

			break

	return (tcp, player)


	#conexao(me, server)

def load_lists(tcp):
	# for i in range (0,8):
	# 	data=tcp.recv(4096)
	# 	character_list.append(data)

	# for i in range (0,24):
	# 	data1=int(tcp.recv(4096))
	# 	data2=int(tcp.recv(4096))
	# 	data3=int(tcp.recv(4096))

	# 	points_list.append((data1, data2, data3))

	# for i in range (0,16):
	# 	data=tcp.recv(4096)
	# 	atack.append(data)

	data=recv_msg(tcp, 65536)

	
	lines = data.split(".")
	del lines[-1]
	
	for item in lines:
		
		line = item.split(",")
		#print line
		character_list.append(line[0][1:])
		points_list.append([int(line[1]), int(line[2]), int(line[3])])
		atack.append([line[4],line[5]])


	

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
			data = recv_msg(tcp, 1024)
			if(len(data) != 0):
				print "Received response: " + str(data)
				break

def send_msg(tcp, msg):
	#mensagem_inicio_conexao = 'Mensagem recebida'
	tcp.send(msg)

def recv_msg(tcp, size_buf):
	return tcp.recv(size_buf)
	
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

def print_chars(unavailable):
	unavailable = unavailable
	for i in range(0, len(character_list)):
		if((i) not in unavailable):
			print str(i + 1) + " " + character_list[i]

def char_to_name(id):
	return character_list[id]


#=========BAN CODE
def ban(tcp, banlist):
	print "\n===SELECT CHARACTER TO BE BANNED==="
	print_chars(banlist)
	print ""
	banned = input("")
	banned = int(banned)
	while banned < 1 or banned > len(character_list) or (banned - 1) in banlist:
		banned = input("sorry, try again ")
		banned = int(banned)

	send_msg(tcp, str(banned - 1))

	print_banned(banned - 1)

	return (banned - 1)

def print_banned(number):
	print "\n" + character_list[number] + " BANNED!"

def recv_ban(tcp):
	banned = int(recv_msg(tcp, 1024))
	
	print_banned(int(banned))

	return banned


#=========PICK CODE
def pick_char(tcp, banlist):
	unavailable = banlist
	print "\n===SELECT CHARACTER TO BE PICKED==="
	print_chars(unavailable)
	print ""

	id_pick = input("")
	id_pick = int(id_pick)
	while id_pick < 1 or id_pick > len(character_list) or (id_pick - 1) in banlist:
		id_pick = input("sorry, try again ")
		id_pick = int(id_pick)

	send_msg(tcp, str(id_pick - 1))

	print_pick(id_pick - 1)

	return (id_pick - 1)

def print_pick(number):
	print "\n" + character_list[number] + " PICKED"

def recv_pick(tcp):
	pick = int(recv_msg(tcp, 1024))

	print_pick(pick)

	return pick



#=========BATTLE
def announce_battle(char1, char2):
	print "BATTLE BETWEEN", char_to_name(char1), "AND", char_to_name(char2), "!!!"

def do_attack(atacante, defensor, tcp):
	print "\n===CHOOSE YOUR MOVE==="
	print "\n=== 0 - " + atack[atacante][0]
	print "\n=== 1 - " + atack[atacante][1]
	print ""
	action = raw_input("")
	action = int(action)
	while action > 1 or action < 0:
		action = raw_input("sorry, try again ")
		action = int(action)

	send_msg(tcp, str(action))

	points_list[defensor][2] -= points_list[atacante][action]
	if points_list[defensor][2] <= 0:
		return 1
	else:
		return 0

def recv_attack(atacante, defensor, tcp):
	print "\n===OPPONENT CHOOSING==="
	print ""

	action = recv_msg(tcp, 1024)

	print "\n===OPPONENT CHOOSED", atack[atacante][int(action)]

	points_list[defensor][2] -= points_list[atacante][int(action)]
	if points_list[defensor][2] <= 0:
		return 1
	else:
		return 0




if __name__ == "__main__":
	
	banlist = []

	numpicks = 3

	team1 = player.Player(numpicks)
	team2 = player.Player(numpicks)

	teams = []
	teams.append(team1)
	teams.append(team2)

	tcp = 0

	initial_print()

	#conexao(me, server)
	tcp, player = server_connect()

	load_lists(tcp)
	
	#test_connection(tcp)
	if(player == 1):
		banned = ban(tcp, banlist)

	elif(player == 2):
		banned = recv_ban(tcp)
	
	banlist.append(banned)

	if(player == 2):
		banned = ban(tcp, banlist)
		

	elif(player == 1):
		banned = recv_ban(tcp)

	banlist.append(banned)

	for i in range(0, numpicks):
		if(player == 1):
			pick = pick_char(tcp, banlist)
			teams[0].add_char(pick)

		elif(player == 2):
			pick = recv_pick(tcp)
			teams[0].add_char(pick)

		banlist.append(pick)

		if(player == 2):
			pick = pick_char(tcp, banlist)
			teams[1].add_char(pick)

		elif(player == 1):
			pick = recv_pick(tcp)
			teams[1].add_char(pick)

		banlist.append(pick)

	teams[0].printTeam(1, character_list)
	teams[1].printTeam(2, character_list)

	
	#BATTLE
	died = 0
	team_dead = False

	while not team_dead:
		announce_battle(teams[0].get_current_char(), teams[1].get_current_char())
		if(player == 2):
			died =do_attack(teams[1].get_current_char(), teams[0].get_current_char(), tcp)

		elif(player == 1):
			died =recv_attack(teams[1].get_current_char(), teams[0].get_current_char(), tcp)

		print character_list[teams[0].get_current_char()], "REMAINING LIFE: ", points_list[teams[0].get_current_char()][2]

		if died == 1:
			print character_list[teams[0].get_current_char()] , "died"
			team_dead = teams[0].update_index()

			if team_dead:
				print "===PLAYER 2 WINS===\n===PLAYER 2 WINS===\n===PLAYER 2 WINS===\n"
				break
			else:
				print character_list[teams[0].get_current_char()], "ready to battle!"




		announce_battle(teams[1].get_current_char(), teams[0].get_current_char())
		if(player == 1):
			died =do_attack(teams[0].get_current_char(), teams[1].get_current_char(), tcp)

		elif(player == 2):
			died =recv_attack(teams[0].get_current_char(), teams[1].get_current_char(), tcp)

		print character_list[teams[1].get_current_char()], "REMAINING LIFE: ", points_list[teams[1].get_current_char()][2]
	 
	 	if died == 1:
			print character_list[teams[1].get_current_char()] , "died"
			team_dead = teams[1].update_index()

			if team_dead:
				print "===PLAYER 1 WINS===\n===PLAYER 1 WINS===\n===PLAYER 1 WINS===\n"
				break
			else:
				print character_list[teams[0].get_current_char()], "ready to battle!"


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
