#!/usr/bin/env python

import os

with open('day1.txt') as f:
	lines = [line.strip() for line in f]

left = []
right = []
capacity = 0

for line in lines:
	parts = [part for part in line.split(' ') if len(part) > 0]
	left.append(int(parts[0]))
	right.append(int(parts[1]))
	capacity = max(capacity, right[-1] + 1)

matches = [0] * capacity

for id_ in right:
	matches[id_] += 1

sum_ = 0

for id_ in left:
	sum_ += id_ * matches[id_]

print(sum_)
