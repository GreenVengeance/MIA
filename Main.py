from random import randint
from Spieler import Spieler

def sp1_ist_am_zug(sp1, sp2):
	print("Spieler1 ist dran:")
	sp1.schuetteln()
	print('Das ist der Wert von Spieler1 eins: ', sp1.result)
	sp1.call = int(input("Zahl eingeben: "))

	random_choice = randint(0, 1)  # 0 = false, 1 = true(glauben)
	if random_choice == 0:
		if sp1.call > sp1.result:
			sp1.punkte = sp1.punkte - 1
			sp1.call = 66
		else:
			sp2.punkte = sp2.punkte - 1
			sp1.call = 66
	else:
		return sp1.call

def sp2_ist_nach_sp1_am_zug(sp1, sp2):
	print("Spieler2 ist dran:")
	sp2.schuetteln()
	random_choice = randint(0, 1)
	if random_choice == 0:
		sp2.call = sp2.result
	elif random_choice == 1:
		sp2.call = sp2.schuetteln()
		while sp2.call < sp2.result:
			sp2.call = sp2.schuetteln()
			if sp2.result == 66:
				break
	print(sp2.call)
	sp1_chioce = (input("Wählen Sie (G)lauben oder (N)icht_Glauebn: "))
	if sp1_chioce == 'N' or sp1_chioce == 'n':
		print(sp2.result)
		if sp2.call < sp1.call:
			sp2.punkte = sp2.punkte - 1
			sp2.call = 66
		else:
			sp1.punkte = sp1.punlte - 1
			sp2.call = 66
	elif sp1_chioce == 'G' or sp1_chioce == 'g':
		return sp2.call
	else:
		print('Unzulässige Eingabe!!!')

def sp1_ist_nach_sp2_am_zug(sp1, sp2):
	print("Spieler1 ist dran:")
	sp1.schuetteln()
	print('Das ist der Wert von Spieler1 eins: ', sp1.result)
	sp1.call = int(input("Zahl eingeben: "))
	while sp1.call < sp2.call:
		sp1.call = int(input("Zahl eingeben: "))

		random_choice = randint(0, 1)  # 0 = false, 1 = true(glauben)
	if random_choice == 0:
		if sp1.call > sp1.result:
			sp1.punkte = sp1.punkte - 1
			sp1.call = 66
		else:
			sp2.punkte = sp2.punkte - 1
			sp1.call = 66
	else:
		return sp1.call

def sp2_ist_am_zug(sp1, sp2):
	print("Spieler2 ist dran:")

	sp2.schuetteln()
	random_choice = randint(0, 1)
	if random_choice == 0:
		sp2.call = sp2.result
	elif random_choice == 1:
		sp2.call = sp2.schuetteln()
		while sp2.call < sp2.result:
			sp2.call = sp2.schuetteln()
			if sp2.result == 66:
				break
	print(sp2.call)

	sp1_chioce = (input("Wählen Sie (G)lauben oder (N)icht_Glauebn: "))
	if sp1_chioce == 'N' or sp1_chioce == 'n':
		if sp2.call > sp2.result:
			sp2.punkte = sp2.punkte - 1
			sp2.call = 66
		else:
			sp1.punkte = sp1.punkte - 1
			sp2.call = 66
	elif sp1_chioce == 'G' or sp1_chioce == 'g':
		return sp2.call
	else:
		print('Unzulässige Eingabe!!!')

def main():
	sp1 = Spieler(input("Wie heißen Sie: "))
	sp2 = Spieler('PC')
	print('Hallo ' + sp1.name + '. Sie spielen jetzt gegen ihren ' + sp2.name + ', das Spiel MIA.')

	random_start = randint(0, 1)
	for round in range(random_start, random_start + 21):
		print("Runde: ", round)
		if sp1.punkte == 0:
			print(sp1.name + ' Sie haben gegen' + sp2 + 'verloren')
			break
		if sp2.punkte == 0:
			print('Glückwunsch' + sp1.name + '!!! Sie haben gewonnen')
			break

		sp1.reset_values()
		sp2.reset_values()
		print('Punktestand: ' + sp1.name + ': ', sp1.punkte, 'und ' + sp2.name + ': ', sp2.punkte)
		print('__________')

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
