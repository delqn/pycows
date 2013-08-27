#!/usr/bin/env python

import random
import sys


def get_bulls_cows(thought, guessed):
	bulls = 0
	cows = 0
	for i in range(0,4):
		if thought[i] == guessed[i]: bulls += 1
		elif thought[i] in guessed: cows += 1
	return bulls, cows

def generate_number():
	result = []
	digits = [x for x in range(0, 10)]
	for count in range(0,4):
		random_position = random.randint(0, len(digits)-1)
		result.append(str(digits[random_position]))
		del digits[random_position]
	return "".join(result)

def get_guess():
	guessed_number = None
	while not guessed_number:
		guessed_number = str(raw_input("Enter your guess: "))
		if len(set(guessed_number)) != 4:
			print "Invalid number: %s" % guessed_number
			guessed_number = None
	return guessed_number

if __name__ == '__main__':
	NUMBER = generate_number()
	guessed = False
	counter = 0
	b = 0
	c = 0
	while b!=4:
		counter += 1
		guessed_number = get_guess()
		b,c = get_bulls_cows(NUMBER, guessed_number)
		print "%s: \tbulls: %s\t cows: %s" % (guessed_number, b, c)
