from network import *

class Card():
	num #2-14
	suit #0-3

def cost_function(a, b):
	if a.num == b.num:
		return numpy.ciel(max(10-b.num,1))
	return 13-a.num + (13-b.num)


def main ():
	#just for preflops right now
	attributes = ["player pos", "player money/bb", "pos size/bb", "bet size/bb", "num player raises", "total num raises", "total players", "players remaining", "player pos in remaining"]
	sizes [ attributes.len(), numpy.ciel(attributes.len() * 1.5), attributes.len(), numpy.ciel(attributes.len() * .5), 1]
	player_profile = Network(sizes)
	dataset = #tuples of the form ([attributes], [card percent])
	

	player_profile.SGD(dataset, 40, 10, .03);


	print(player.evaluate(dataset)

