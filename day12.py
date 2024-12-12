#!/usr/bin/env python

def recurse(x, y, plant):
	cell = (x, y)

	if x < 0 or x == w or y < 0 or y == h or lines[y][x] != plant:
		return False

	if cell in covered:
		return True

	covered.add(cell)
	top = recurse(x, y - 1, plant)
	bottom = recurse(x, y + 1, plant)
	left = recurse(x - 1, y, plant)
	right = recurse(x + 1, y, plant)

	if top and bottom and left and right:
		open_sides = 0
	elif top and bottom and left:
		open_sides = 1
	elif top and bottom and right:
		open_sides = 1
	elif top and left and right:
		open_sides = 1
	elif bottom and left and right:
		open_sides = 1
	elif top and bottom:
		open_sides = 2
	elif top and left:
		open_sides = 2
	elif top and right:
		open_sides = 2
	elif left and right:
		open_sides = 2
	elif left and bottom:
		open_sides = 2
	elif bottom and right:
		open_sides = 2
	elif top or bottom or left or right:
		open_sides = 3
	else:
		open_sides = 4

	region.append(open_sides)

	return True

with open('day12.txt') as f:
	lines = [line.strip() for line in f]

covered = set()
w = len(lines[0])
h = len(lines)
total = 0

for y in range(h):
	for x in range(w):
		if not (x, y) in covered:
			plant = lines[y][x]
			region = []
			
			recurse(x, y, plant)

			area = len(region)
			perimeter = sum(open_sides for open_sides in region)
			cost = area * perimeter

			total += cost

print(total)
