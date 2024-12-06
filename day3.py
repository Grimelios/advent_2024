#!/usr/bin/env python

import os

with open('day3.txt') as f:
	lines = [line.strip() for line in f]

sum_ = 0
mul_enabled = True

for line in lines:
	i = 0

	while i < len(line):
		if not mul_enabled:
			do = line.find('do()', i)

			if do == -1:
				break

			mul_enabled = True
			i = do + 4

		if i < len(line) - 7 and line[i:(i + 7)] == 'don\'t()':
			i += 7
			mul_enabled = False

			continue

		if not (i < len(line) - 4 and line[i:(i + 4)] == 'mul('):
			i += 1

			continue

		i += 4
		comma = line.find(',', i)

		if comma == -1:
			break

		try:
			a = int(line[i:comma])
		except ValueError:
			continue

		i = comma + 1
		closing_paren = line.find(')', i)

		if closing_paren == -1:
			break

		try:
			b = int(line[i:closing_paren])
		except ValueError:
			continue

		sum_ += a * b
		i = closing_paren + 1

print(sum_)
