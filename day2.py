#!/usr/bin/env python

import os

def evaluate(report, depth):
	required_sign = sign(report[1] - report[0])

	for i in range(len(report) - 1):
		a = report[i]
		b = report[i + 1]
		delta = b - a

		if sign(delta) == required_sign and abs(delta) > 0 and abs(delta) < 4:
			continue

		if depth == 1:
			return False

		if i > 0:
			modified = []
			modified.extend(report[:(i - 1)])
			modified.extend(report[i:])

			if evaluate(modified, 1):
				return True

		modified = []
		modified.extend(report[:i])
		modified.extend(report[(i + 1):])

		if evaluate(modified, 1):
			return True

		if i < len(report) - 1:
			modified = []
			modified.extend(report[:(i + 1)])
			modified.extend(report[(i + 2):])

			if evaluate(modified, 1):
				return True

		return False

	return True

def sign(value):
	return 1 if value > 0 else -1

with open('day2.txt') as f:
	lines = [line.strip() for line in f]

total_safe = 0

for line in lines:
	report = [int(part) for part in line.split(' ')]

	if evaluate(report, 0):
		total_safe += 1

print(total_safe)
