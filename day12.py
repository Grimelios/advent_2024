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
	corners = 0

	if not top and not left:
		corners += 1

	if not top and not right:
		corners += 1

	if not left and not bottom:
		corners += 1

	if not right and not bottom:
		corners += 1

	if top and left and lines[y - 1][x - 1] != plant:
		corners += 1

	if top and right and lines[y - 1][x + 1] != plant:
		corners += 1

	if left and bottom and lines[y + 1][x - 1] != plant:
		corners += 1

	if right and bottom and lines[y + 1][x + 1] != plant:
		corners += 1

	region.append(corners)

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
			sides = sum(corners for corners in region)
			cost = area * sides
			total += cost

print(total)
