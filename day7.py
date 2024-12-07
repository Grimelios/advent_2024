#!/usr/bin/env python

import types

tt = types.SimpleNamespace()
tt.OP_CONCAT = '||'
tt.OP_MUL = '*'
tt.OP_PLUS = '+'

def evaluate(values, ops):
	for i in range(len(values) - 1):
		a = values[i]
		b = values[i + 1]

		if i == 0:
			match ops[i]:
				case tt.OP_CONCAT: result = int(str(a) + str(b))
				case tt.OP_MUL: result = a * b
				case tt.OP_PLUS: result = a + b
		else:
			match ops[i]:
				case tt.OP_CONCAT: result = int(str(result) + str(b))
				case tt.OP_MUL: result *= b
				case tt.OP_PLUS: result += b

	return result

def recurse(values, ops, expected, i):
	if i == len(values) - 1:
		evaluated = evaluate(values, ops)

		return evaluate(values, ops) == expected

	ops[i] = tt.OP_PLUS

	if recurse(values, ops, expected, i + 1):
		return True

	ops[i] = tt.OP_MUL

	if recurse(values, ops, expected, i + 1):
		return True

	ops[i] = tt.OP_CONCAT

	return recurse(values, ops, expected, i + 1)

with open('day7.txt') as f:
	lines = [line.strip() for line in f]

sum_ = 0

for line in lines:
	parts = line.split(':')
	expected = int(parts[0])
	values = [int(part) for part in parts[1][1:].split(' ')]
	ops = [None] * (len(values) - 1)

	if recurse(values, ops, expected, 0):
		sum_ += expected

print(sum_)
