#!/usr/bin/env python

def recurse(x, y, current):
	if current == 9:
		return 1

	sum_ = 0

	if x > 0 and topological[y][x - 1] == current + 1:
		sum_ += recurse(x - 1, y, current + 1)

	if x < w - 1  and topological[y][x + 1] == current + 1:
		sum_ += recurse(x + 1, y, current + 1)

	if y > 0 and topological[y - 1][x] == current + 1:
		sum_ += recurse(x, y - 1, current + 1)

	if y < h - 1 and topological[y + 1][x] == current + 1:
		sum_ += recurse(x, y + 1, current + 1)

	return sum_

with open('day10.txt') as f:
	topological = [[int(c) for c in line.strip()] for line in f]

w = len(topological[0])
h = len(topological)
sum_ = 0

for y in range(h):
	for x in range(w):
		if topological[y][x] == 0:
			sum_ += recurse(x, y, 0)

print(sum_)
