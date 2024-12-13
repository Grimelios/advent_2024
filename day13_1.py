#!/usr/bin/env python

A_COST = 3
B_COST = 1
MAX_PRESSES_PER_BUTTON = 100

class Cell:
	def __init__(self, line):
		line = line[line.find(':') + 1:]
		parts = [part.lstrip() for part in line.split(',')]

		self.x = int(parts[0][2:])
		self.y = int(parts[1][2:])

	def __str__(self):
		return f'[{self.x}, {self.y}]'

class Machine:
	def __init__(self, a, b, prize):
		self.a = a
		self.b = b
		self.prize = prize

def analyze(machine):
	min_cost = None

	for i in range(MAX_PRESSES_PER_BUTTON + 1):
		for j in range(MAX_PRESSES_PER_BUTTON + 1):
			x_from_a = machine.a.x * i
			y_from_a = machine.a.y * i
			x_from_b = machine.b.x * j
			y_from_b = machine.b.y * j

			if (
				x_from_a + x_from_b == machine.prize.x and
				y_from_a + y_from_b == machine.prize.y):

				cost = i * A_COST + j * B_COST
				min_cost = cost if min_cost is None else min(cost, min_cost)

	return min_cost if min_cost is not None else 0

with open('day13.txt') as f:
	lines = [line.strip() for line in f]

machines = []

for i in range(0, len(lines), 4):
	a = Cell(lines[i])
	b = Cell(lines[i + 1])
	prize = Cell(lines[i + 2])
	machines.append(Machine(a, b, prize))

tokens = 0

for machine in machines:
	tokens += analyze(machine)

print(tokens)
