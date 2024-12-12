#!/usr/bin/env python

with open('day11.txt') as f:
	lines = [line for line in f]
	stones = [int(part) for part in lines[0].split(' ')]

for i in range(25):
	next_ = []

	for i, stone in enumerate(stones):
		if stone == 0:
			next_.append(1)
		else:
			str_ = str(stone)

			if len(str_) % 2 == 0:
				left = str_[:len(str_) // 2]
				right = str_[len(str_) // 2:]
				next_.append(int(left))
				next_.append(int(right))
			else:
				next_.append(stone * 2024)

	stones = next_

print(len(stones))
