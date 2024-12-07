#!/usr/bin/env python

def evaluate(values, ops):
	for i in range(len(values) - 1):
		a = values[i]
		b = values[i + 1]

		if i == 0:
			result = a + b if ops[i] == '+' else a * b
		else:
			result = result + b if ops[i] == '+' else result * b

	return result

def recurse(values, ops, expected, i):
	if i == len(values) - 1:
		evaluated = evaluate(values, ops)

		return evaluate(values, ops) == expected

	ops[i] = '+'

	if recurse(values, ops, expected, i + 1):
		return True

	ops[i] = '*'	

	return recurse(values, ops, expected, i + 1)

with open('day7.txt') as f:
	lines = [line.strip() for line in f]

sum_ = 0

for line in lines:
	parts = line.split(':')
	expected = int(parts[0])
	values = [int(part) for part in parts[1][1:].split(' ')]
	ops = ['+'] * (len(values) - 1)

	if recurse(values, ops, expected, 0):
		sum_ += expected

print(sum_)
