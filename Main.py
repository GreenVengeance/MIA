from random import randint
from Spieler import Spieler

def sp1_ist_am_zug(sp1, sp2):
	print('__________')
	print(sp1.name + " ist dran.")
	sp1.schuetteln()
	result: int = sp1.result
	print(sp1.name + " würfelt:", result)
	sp1_chioce = (input("Möchten bluffen: (y)es or (n)o: "))
	if sp1_chioce == 'Y' or sp1_chioce == 'y':
		sp1.call: int = int(input("Geben Sie eine Zahl ein, wenn Sie bluffen möchten: "))
	elif sp1_chioce == 'N' or sp1_chioce == 'n':
		sp1.call = sp1.result
	else:
		print("unzulässige Eingabe, Sie werden disqualifiziert")
		sp1.punkte = 0
	random_choice = randint(0, 1)  # 0 = false, 1 = true(glauben)
	if random_choice == 0:
		if sp1.call > result:
			sp1.punkte = sp1.punkte - 1
			print(sp1.name + " verliert einen Punkt!!!")
			sp1.call = 66
		else:
			sp2.punkte = sp2.punkte - 1
			print(sp2.name + " verliert einen Punkt!!!")
			sp1.call = 66
	else:
		print("Der " + sp2.name + " hat hat Ihnen geglaubt")
		return sp1.call

def sp2_ist_nach_sp1_am_zug(sp1, sp2):
	print('__________')
	print(sp2.name + " ist dran.")
	sp2.schuetteln()
	result: int = sp2.result
	random_choice = randint(0, 1)
	if random_choice == 0:
		sp2.call = result
		while sp2.result <= sp1.call:
			sp2.schuetteln()
			sp2.call = sp2.result
			if sp2.result == 66:
				break
	elif random_choice == 1:
		sp2.schuetteln()
		sp2.call = sp2.result
		while sp2.call <= sp1.call:
			sp2.schuetteln()
			sp2.call = sp2.result
			if sp2.result == 66:
				break

	print(sp2.name + " würfelt:", sp2.call)
	sp1_chioce = (input("Möchten Sie ihrem gegenueber glauben: (y)es or (n)o: "))
	if sp1_chioce == 'N' or sp1_chioce == 'n':
		print(result)
		if sp2.call < result:
			sp2.punkte = sp2.punkte - 1
			print(sp2.name + " verliert einen Punkt!!!")
			sp2.call = 66
		else:
			sp1.punkte = sp1.punkte - 1
			print(sp1.name + " verliert einen Punkt!!!")
			sp2.call = 66
	elif sp1_chioce == 'Y' or sp1_chioce == 'y':
		return sp2.call
	else:
		print("Unzulässige Eingabe!!!")

def sp1_ist_nach_sp2_am_zug(sp1, sp2):
	print('__________')
	print(sp1.name + " ist dran.")
	sp1.schuetteln()
	result: int = sp1.result
	print(sp1.name + " würfelt: ", result)
	sp1_chioce = (input("Möchten bluffen: (y)es or (n)o: "))
	if sp1_chioce == 'Y' or sp1_chioce == 'y':
		sp1.call: int = int(input("Geben Sie eine Zahl ein, wenn Sie bluffen möchten: "))
	elif sp1_chioce == 'N' or sp1_chioce == 'n':
		sp1.call = sp1.result
	else:
		print("unzulässige Eingabe, Sie werden disqualifiziert")
		sp1.punkte = 0
	random_choice = randint(0, 1)  # 0 = false, 1 = true(glauben)
	if random_choice == 0:
		if sp1.call > result:
			sp1.punkte = sp1.punkte - 1
			print(sp1.name + " verliert einen Punkt!!!")
			sp1.call = 66
		else:
			sp2.punkte = sp2.punkte - 1
			print(sp2.name + " verliert einen Punkt!!!")
			sp1.call = 66
	else:
		print("Der " + sp2.name + " hat hat Ihnen geglaubt")
		return sp1.call

def sp2_ist_am_zug(sp1, sp2):
	print('__________')
	print(sp2.name + " ist dran.")
	sp2.schuetteln()
	result: int = sp2.result
	random_choice = randint(0, 1)
	if random_choice == 0:
		sp2.call = result
		while sp2.result <= sp1.call:
			sp2.schuetteln()
			sp2.call = sp2.result
	elif random_choice == 1:
		sp2.schuetteln()
		sp2.call = sp2.result
		while sp2.call <= sp1.call:
			sp2.schuetteln()
			sp2.call = sp2.result
			if sp2.result == 66:
				break
	print(sp2.name + ' würfelt: ', sp2.call)
	sp1_chioce = (input("Möchten Sie ihrem gegenueber glauben: (y)es or (n)o: "))
	if sp1_chioce == 'N' or sp1_chioce == 'n':
		if sp2.call > result:
			sp2.punkte = sp2.punkte - 1
			print(sp2.name + ' verliert einen Punkt!!!')
			sp2.call = 66
		else:
			sp1.punkte = sp1.punkte - 1
			print(sp1.name + ' verliert einen Punkt!!!')
			sp2.call = 66
	elif sp1_chioce == 'Y' or sp1_chioce == 'y':
		return sp2.call
	else:
		print('Unzulässige Eingabe!!!')

def main():
	sp1 = Spieler(str(input("Wie heißen Sie: ")))
	sp2 = Spieler('PC')
	print('Hallo ' + sp1.name + '. Sie spielen jetzt gegen ihren ' + sp2.name + ', das Spiel MIA.')

	for round in range(1,  21):
		print("Runde: ", round)
		if sp1.punkte == 0:
			print(sp1.name + ', Sie haben gegen: ' + sp2.name + ' verloren')
			break
		if sp2.punkte == 0:
			print('Glückwunsch' + sp1.name + '!!! Sie haben gewonnen')
			break

		sp1.reset_values()
		sp2.reset_values()
		print('Punktestand: ' + sp1.name + ':', sp1.punkte, 'und ' + sp2.name + ':', sp2.punkte)

		if round % 2 == 0:
			sp1_ist_am_zug(sp1, sp2)
			if sp1.call != 66:
				while sp1.call != 66 or sp2.call != 66:
					sp2_ist_nach_sp1_am_zug(sp1, sp2)
					if sp2.call != 66:
						sp1_ist_nach_sp2_am_zug(sp1, sp2)
					else:
						print('__________')
						break
			else:
				print('__________')
				continue

		else:
			sp2_ist_am_zug(sp1, sp2)
			if sp2.call != 66:
				while sp1.call != 66 or sp2.call != 66:
					sp1_ist_nach_sp2_am_zug(sp1, sp2)
					if sp1.call != 66:
						sp2_ist_nach_sp1_am_zug(sp1, sp2)
					else:
						print('__________')
						break
			else:
				print('__________')
				continue


if __name__ == '__main__':
	main()
