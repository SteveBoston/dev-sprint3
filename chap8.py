# This is where the answers to Chapter 8 questions for the BSS Dev RampUp go
# Name: Steve Gallagher


# 8.12

import sys


def rotate_word(word, num):
	for letter in word:
		e = ord(letter)
		f = e + num
		g = chr(f)
		sys.stdout.write(g)


rotate_word("thisisalongtestword", 2)


def undo(word, num):
	for letter in word:
		z = ord(letter)
		y = z - num
		x = chr(y)
		sys.stdout.write(x)


#undo("vjkukucnqpivguvyqtf", 2)