import player
import sys

#Mercedes = car.Car('Mercedes', 'S Class', 'Red')
#
#print (Mercedes.color)

character_list = ["Marilton", "Paulo", "Torchelsen", "Pilla", "Leomar", "Luciana", "Simone", "Rafa", "Tati", "Guilherme", "Porto", "Lisane", "Felipe", "Substituto", "Cesar Menotti", "Du Bois", "Renata", "Gerson", "Ferrugem", "Ana"]

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

if __name__ == "__main__":
	
	initial_print()
	while (sys.stdin.read(1) != "\n"):
		pass
	banlist = []
	player1 = player.Player(3)
	player2 = player.Player(3)

	banlist.append(ban())

	for i in range(0, 2):
		p1char = pick_char(banlist)
		player1.add_char(p1char)
		banlist.append(p1char)

		p2char = pick_char(banlist)
		player2.add_char(p2char)
		banlist.append(p2char)

	print ""
	player1.printTeam()
	player2.printTeam()
	print "======="
	