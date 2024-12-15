#!/usr/bin/env python

WIDTH = 101
HEIGHT = 103
SIMULATE = 100

class Robot:
	def __init__(self, p, v):
		self.p = p
		self.v = v

	def move(self):
		self.p.x += self.v.x
		self.p.y += self.v.y

		if self.p.x < 0:
			self.p.x += WIDTH
		elif self.p.x >= WIDTH:
			self.p.x -= WIDTH

		if self.p.y < 0:
			self.p.y += HEIGHT
		elif self.p.y >= HEIGHT:
			self.p.y -= HEIGHT

class Vector:
	def __init__(self, part):
		parts = part[2:].split(',')

		self.x = int(parts[0])
		self.y = int(parts[1])

	def __str__(self):
		return f'[{self.x}, {self.y}]'

def analyze_quadrant(x, y):
	robots_in_quadrant = 0

	for robot in robots:
		if robot.p.x >= x and robot.p.x < x + WIDTH // 2 and robot.p.y >= y and robot.p.y < y + HEIGHT //2:
			robots_in_quadrant += 1

	return robots_in_quadrant

with open('day14.txt') as f:
	lines = [line.strip() for line in f]

robots = []

for line in lines:
	parts = line.split(' ')
	p = Vector(parts[0])
	v = Vector(parts[1])
	robots.append(Robot(p, v))

for i in range(SIMULATE):
	for robot in robots:
		robot.move()

safety_factor = 1

for i in range(2):
	for j in range(2):
		x = j * WIDTH // 2 + j
		y = i * HEIGHT // 2 + i
		robots_in_quadrant = analyze_quadrant(x, y)
		safety_factor *= robots_in_quadrant

print(safety_factor)
