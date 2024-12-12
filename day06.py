#!/usr/bin/env python

import os

def check_loop(lines, start_x, start_y):
	p_x = start_x
	p_y = start_y
	v_x = 0
	v_y = -1
	covered = { }

	while True:
		p = (p_x, p_y)
		v = (v_x, v_y)
		
		if not p in covered:
			covered[p] = []
		elif v in covered[p]:
			return True

		covered[p].append(v)

		while True:
			tentative_x = p_x + v_x
			tentative_y = p_y + v_y

			if not (tentative_x >= 0 and tentative_x < w and tentative_y >= 0 and tentative_y < h):
				return False

			if lines[tentative_y][tentative_x] == '#':
				v_x, v_y = rotate(v_x, v_y)
			else:
				break

		p_x += v_x
		p_y += v_y

def rotate(v_x, v_y):
	if v_x == 0 and v_y == -1:
		return (1, 0)

	if v_x == 1 and v_y == 0:
		return (0, 1)

	if v_x == 0 and v_y == 1:
		return (-1, 0)
	
	return (0, -1)

with open('day06.txt') as f:
	lines = [[c for c in line.strip()] for line in f]

w = len(lines[0])
h = len(lines)

for y in range(h):
	done = False

	for x in range(w):
		if lines[y][x] == '^':
			start_x = x
			start_y = y
			done = True

			break

	if done:
		break

potential_obstacles = []

for y in range(h):
	for x in range(w):
		if lines[y][x] == '.':
			potential_obstacles.append((x, y))

potential_obstacles_that_loop = 0

for x, y in potential_obstacles:
	lines[y][x] = '#'

	if check_loop(lines, start_x, start_y):
		potential_obstacles_that_loop += 1

	lines[y][x] = '.'

print(potential_obstacles_that_loop)
