#!/usr/bin/env python

DOT = '.'

with open('day09.txt') as f:
	lines = [line.strip() for line in f]

blocks = []
id_ = 0

for i, c in enumerate(lines[0]):
	if i % 2 == 0:
		for j in range(int(c)):
			blocks.append(id_)

		id_ += 1
	else:
		for j in range(int(c)):
			blocks.append(DOT)

a = 0
b = len(blocks) - 1

while a < b:
	while a < b and blocks[a] != DOT:
		a += 1

	while a < b and blocks[b] == DOT:
		b -= 1

	blocks[a] = blocks[b]
	blocks[b] = DOT

checksum = 0

for i, block in enumerate(blocks):
	if block == DOT:
		break

	checksum += block * i

print(checksum)
	