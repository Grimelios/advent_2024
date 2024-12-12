#!/usr/bin/env python

with open('day8.txt') as f:
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
	for i in range(len(coords)):
		for j in range(len(coords)):
			if i == j:
				continue

			a = coords[i]
			b = coords[j]
			dx = b[0] - a[0]
			dy = b[1] - a[1]
			nx = b[0] + dx
			ny = b[1] + dy

			if nx >= 0 and nx < w and ny >= 0 and ny < h and not antinodes[ny][nx]:
				antinodes[ny][nx] = True
				unique += 1

print(unique)
