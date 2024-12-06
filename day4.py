#!/usr/bin/env python

import os

MAS = 'MAS'
SAM = 'SAM'

with open('day4.txt') as f:
	lines = [line.strip() for line in f]

total = 0

for y in range(len(lines) - 2):
	for x in range(len(lines[y]) - 2):
		has_DR = True
		has_DL = True

		for i in range(3):
			if lines[y + i][x + i] != MAS[i]:
				has_DR = False

				break

		if not has_DR:
			has_DR = True


			for i in range(3):
				if lines[y + i][x + i] != SAM[i]:
					has_DR = False

					break

		for i in range(3):
			for i in range(3):
				if lines[y + i][x + 2 - i] != MAS[i]:
					has_DL = False

					break

		if not has_DL:
			has_DL = True

			for i in range(3):
				if lines[y + i][x + 2 - i] != SAM[i]:
					has_DL = False

					break

		if has_DR and has_DL:
			total += 1

print(total)
