import player
import sys

#Mercedes = car.Car('Mercedes', 'S Class', 'Red')
#
#print (Mercedes.color)

#character_list = ["Marilton", "Paulo", "Torchelsen", "Pilla", "Leomar", "Luciana", "Simone", "Rafa", "Tati", "Guilherme", "Porto", "Lisane", "Felipe", "Substituto", "Cesar Menotti", "Du Bois", "Renata", "Gerson", "Ferrugem", "Ana"]
#points_list = [[3,2,5],[3,2,5],[3,2,5],[3,2,5],[3,2,5],[3,2,5],[3,2,10],[3,2,10],[3,2,10],[3,2,10],[3,2,10],[3,2,10],[3,2,10],[3,2,10],[3,2,10],[3,2,10],[3,2,10],[3,2,10],[3,2,10],[3,2,10] ]

character_list = []
points_list = []
atack = []
file = open("entrada.txt","r")


for item in file:
	line = item.split(",")
	character_list.append(line[0])
	points_list.append([int(line[1]), int(line[2]), int(line[3])])
	atack.append([line[4],line[5][:-1]])

def initial_print():
	print "================================================================"
	print "========================WELCOME TO PROFMON======================"
	print "================================================================"
	print "."
	print "."
	print "."
	print "Waiting for other player to connect"
	print "."
	print "."
	print "."
	print "Other player connected!"
	print "\nSTARTING DRAFT!!!\n"
	print "Press ENTER to continue\n"

def ban():
	print "===SELECT CHARACTER TO BE BANNED==="
	print_chars([])
	print ""
	banned = input("")
	print "\n" + character_list[banned - 1] + " BANNED"
	return banned

def print_chars(unavailable):
	unavailable = unavailable
	for i in range(0, len(character_list)):
		if((i + 1) not in unavailable):
			print str(i + 1) + " " + character_list[i]

def pick_char(banlist):
	unavailable = banlist
	print "\n===SELECT CHARACTER TO BE PICKED==="
	print_chars(unavailable)
	print ""
	id_pick = input("")
	print "\n" + character_list[id_pick - 1] + " PICKED"
	return id_pick

def start_game():
	print "===SELECT CHARACTER TO PLAY==="
	print ""
	id_pick = input("")
	return id_pick

def action(charp1, charp2):
	print "\n===CHOOSE OPTION==="
	print "\n=== 0 - " + atack[character_list.index(charp2)][0]
	print "\n=== 1 - " + atack[character_list.index(charp2)][1]
	print ""
	id_action = input("")
	points_list[character_list.index(charp1)][2] -= points_list[character_list.index(charp2)][id_action]
	if points_list[character_list.index(charp1)][2] < 0:
		return 0
	else:
		return 1

if __name__ == "__main__":
	
	initial_print()
	while (sys.stdin.read(1) != "\n"):
		pass
	banlist = []
	player1 = player.Player(2)
	player2 = player.Player(2)

	banlist.append(ban())

	for i in range(0, 2):
		p1char = pick_char(banlist)
		player1.add_char(character_list[p1char-1])
		banlist.append(p1char)

		p2char = pick_char(banlist)
		player2.add_char(character_list[p2char-1])
		banlist.append(p2char)

	print ""
	player1.printTeam()
	player2.printTeam()
	print "======= START GAME ======= "
	r1 = 1
	r2 = 1

	p1char = start_game()
	player1.set_char(p1char)
	p2char = start_game()
	player2.set_char(p2char)

	while True:
		if r1 == 0:
			print "\n===YOUR CHARACTER DIED P1===\n"
			team = player1.remove_char()

			if(team > 0):
				player1.printTeam()
				p1char = start_game()
				player1.set_char(p1char)
			else:
				print "\n===GAME OVER==="
				print "\n===P2 WINS==="				
				break

		if r2 == 0:
			print "\n===YOUR CHARACTER DIED P2==="
			team = player2.remove_char()

			if(team > 0):
				player2.printTeam()
				p2char = start_game()
				player2.set_char(p2char)
			else:
				print "\n===GAME OVER==="
				print "\n===P1 WINS==="
				break
			
		while True:
			r1 = action(player1.get_char_name(), player2.get_char_name())
			if(r1 == 0):
				break
			r2 = action(player2.get_char_name(), player1.get_char_name())
			if r2 == 0:
				break

		
			
			


	