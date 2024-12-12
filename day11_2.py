#!/usr/bin/env python

BLINKS = 75

def recurse(stone, depth):
	if depth == BLINKS:
		return 1

	key = (stone, depth)

	if key in lookup:
		return lookup[key]

	if stone == 0:
		value = recurse(1, depth + 1)
	else:
		str_ = str(stone)

		if len(str_) % 2 == 0:
			left = str_[:len(str_) // 2]
			right = str_[len(str_) // 2:]
			value = recurse(int(left), depth + 1) + recurse(int(right), depth + 1)
		else:
			value = recurse(stone * 2024, depth + 1)

	lookup[key] = value

	return value

with open('day11.txt') as f:
	lines = [line for line in f]
	stones = [int(part) for part in lines[0].split(' ')]

sum_ = 0
lookup = { }

for stone in stones:
	sum_ += recurse(stone, 0)

print(sum_)
