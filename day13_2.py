#!/usr/bin/env python

A_COST = 3
B_COST = 1
PRIZE_ERROR = 10000000000000

class Cell:
	def __init__(self, line, error):
		line = line[line.find(':') + 1:]
		parts = [part.lstrip() for part in line.split(',')]

		self.x = int(parts[0][2:]) + error
		self.y = int(parts[1][2:]) + error

	def __str__(self):
		return f'[{self.x}, {self.y}]'

class Line:
	def __init__(self, a, b):
		self.a = a
		self.b = b
		self.v = b - a

	def __str__(self):
		return f'{self.a} -> {self.b}'

class Machine:
	def __init__(self, a, b, prize):
		self.a = a
		self.b = b
		self.prize = prize

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __add__(self, other):
		return Point(self.x + other.x, self.y + other.y)

	def __str__(self):
		return f'[{self.x}, {self.y}]'

	def __sub__(self, other):
		return Point(self.x - other.x, self.y - other.y)

def analyze(machine):
	a = Line(
		Point(0, 0), 
		Point(machine.a.x, machine.a.y))

	b = Line(
		Point(machine.prize.x, machine.prize.y), 
		Point(machine.prize.x - machine.b.x, machine.prize.y - machine.b.y))

	e1 = coefficients(a)
	e2 = coefficients(b)
	det = e1[0] * e2[1] - e1[1] * e2[0]
	x = e1[2] * e2[1] - e1[1] * e2[2]
	y = e1[0] * e2[2] - e1[2] * e2[0]
	intersect = Point(x / det, y / det)
	intersect.x = abs(intersect.x)
	intersect.y = abs(intersect.y)
	
	if (int(intersect.x) == intersect.x and 
		int(intersect.y) == intersect.y and 
		int(intersect.x) % machine.a.x == 0 and
		int(intersect.y) % machine.a.y == 0):

		a_presses = int(intersect.x / machine.a.x)
		b_presses = int((machine.prize.x - intersect.x) / machine.b.x)
		
		return a_presses * A_COST + b_presses * B_COST

	return 0

def coefficients(line):
	det = determinant(line.a, line.b)

	return (-line.v.y, line.v.x, -det)

def determinant(a, b):
	return a.x * b.y - b.x * a.y

with open('day13.txt') as f:
	lines = [line.strip() for line in f]

machines = []

for i in range(0, len(lines), 4):
	a = Cell(lines[i], 0)
	b = Cell(lines[i + 1], 0)
	prize = Cell(lines[i + 2], PRIZE_ERROR)
	machines.append(Machine(a, b, prize))

tokens = 0

for machine in machines:
	tokens += analyze(machine)

print(tokens)
