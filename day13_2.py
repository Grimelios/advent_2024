#!/usr/bin/env python

A_COST = 3
B_COST = 1
#PRIZE_ERROR = 10000000000000
PRIZE_ERROR = 0

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
		self.v = Point(b.x - a.x, b.y - a.y)

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

	def __str__(self):
		return f'[{self.x}, {self.y}]'

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

	print(f'A {a}')
	print(f'B {b}')
	print(f'INTERSECT {intersect}')

	return 0

def coefficients(line):
	det = determinant(line.a, b)

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
