#!/usr/bin/env python

with open('day08.txt') as f:
	lines = [line.strip() for line in f]

w = len(lines[0])
h = len(lines)
antennas = { }
antinodes = []

for y in range(h):
	antinodes.append([False] * w)

	for x in range(w):
		c = lines[y][x]

		if c == '.':
			continue

		antennas.setdefault(c, [])
		antennas[c].append((x, y))

unique = 0

for key, coords in antennas.items():
	if len(coords) == 1:
		continue

	for i in range(len(coords)):
		for j in range(len(coords)):
			if i == j:
				continue

			ax, ay = coords[i]
			bx, by = coords[j]
			dx = bx - ax
			dy = by - ay
			nx = bx
			ny = by

			while True:
				if not antinodes[ny][nx]:
					antinodes[ny][nx] = True
					unique += 1
					
				nx += dx
				ny += dy

				if not (nx >= 0 and nx < w and ny >= 0 and ny < h):
					break

print(unique)
