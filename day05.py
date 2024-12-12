#!/usr/bin/env python

import os

with open('day05.txt') as f:
	lines = [line.strip() for line in f]

i = 0
must_come_after = { }

while i < len(lines):
	line = lines[i]
	i += 1

	if len(line) == 0:
		break

	parts = line.split('|')
	x = int(parts[0])
	y = int(parts[1])
	must_come_after.setdefault(y, set())
	must_come_after.setdefault(x, set())
	must_come_after[y].add(x)

sum_ = 0

while i < len(lines):
	pages = [int(part) for part in lines[i].split(',')]
	i += 1
	already_in_order = True

	for j in range(len(pages)):
		first = pages[j]

		for k in range(j + 1, len(pages)):
			second = pages[k]

			if second in must_come_after[first]:
				already_in_order = False

				break

		if not already_in_order:
			break

	if already_in_order:
		continue

	for j in range(len(pages) - 1):
		no_swaps = True

		for k in range(len(pages) - j - 1):
			first = pages[k]
			second = pages[k + 1]

			if second in must_come_after[first]:
				pages[k] = second
				pages[k + 1] = first
				no_swaps = False

		if no_swaps:
			break
	
	sum_ += pages[len(pages) // 2]

print(sum_)
