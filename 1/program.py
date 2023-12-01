import os
import sys

red = 12
green = 13
blue = 14

colors = ['red', 'green', 'blue']

g = {'red': 12, 'green': 13, 'blue': 14}

games = set()

with open("input.txt") as file:
	lines = file.readlines()
	for line in lines:
		print(line)
		parsed = line.split(':')
		game = parsed[0].split(' ')[1]
		print(game)
		games.add(int(game))
		draws = parsed[1].strip().split(';')
		min_req = {'red': 0, 'green': 0, 'blue': 0}
		for draw in draws:
			draw = draw.strip().split(',')
			for item in draw:
				item = item.strip()
				print(item)
				for color in colors:
					indx = item.find(color)
					if indx != -1:
						number = item[0:indx]
						num_to_check = g[color]
						if min_req[color] < int(number):
							min_req[color] = int(number)
						
		print(min_req)
		product = 1
		for item in min_req.values():
			product *= item
		print(product)
	print(games)
	sum = 0
	for item in games:
		sum += item
	print(sum)
