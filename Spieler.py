from random import randint

class Spieler:

	'''Konstruktor'''
	def __init__(self, name):
		self.name = name
		self.punkte = 10
		self.result = 0
		self.call = 0

	def schuetteln(self):
		random_zahl1 = randint(1, 6)
		random_zahl2 = randint(1, 6)
		if random_zahl1 > random_zahl2:
			self.result = (random_zahl1 * 10) + random_zahl2
		else:
			self.result = (random_zahl2 * 10) + random_zahl1

	def reset_values(self):
		self.result = 0
		self.call = 0
