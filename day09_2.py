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

b = len(blocks) - 1

while True:
	while blocks[b] == DOT:
		b -= 1

	a = 0

	while blocks[a] != DOT:
		a += 1

	if a > b:
		break

	id_ = blocks[b]
	required = 0

	while blocks[b - required] == id_:
		required += 1

	while a < b:
		available = 0

		while blocks[a + available] == DOT:
			available += 1

		if available >= required:
			for i in range(required):
				blocks[a + i] = id_
				blocks[b - i] = DOT

			break

		a += available

		while blocks[a] != DOT:
			a += 1

	while blocks[b] == id_:
		b -= 1

	while blocks[b] == DOT:
		b -= 1

checksum = 0

for i, block in enumerate(blocks):
	if block != DOT:
		checksum += block * i

print(checksum)
	