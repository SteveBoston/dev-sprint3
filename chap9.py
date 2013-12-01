# This is where the answers to Chapter 9 questions for the BSS Dev RampUp go
# Name: Steve Gallagher

from __future__ import division
import math



fin = open('words.txt')




# 9.1




def twentyletters():
	for word in fin:
		if len(word) > 20:
			print word

#twentyletters()




# 9.2




def has_no_e(word):

	if not "e" in word:
		print word
		return True

#has_no_e(word)




def printer():
	for word in fin:
		has_no_e(word)

#printer()


count = 0

overall = 0

def per(count, overall):
	for word in fin:
		overall = overall + 1
		print "Total number of words is", overall
		if not "e" in word:
			count = count + 1
			print "Number of words without an 'e' is", count

#per(count, overall)

#percentage of words without e is: (37642/113809)*100, "%"    which is around 33%




# 9.3



def avoids(word, string):

	n = 0

	def checker(word, string, n):
		if n < len(string):
			sub = string[n]
			if word.count(sub, 0, len(word)) == 0:
				n = n + 1
				checker(word, string, n)

			elif word.count(sub, 0, len(word)) != 0:
				return False

		else:
			print word
			return True
				
	checker(word, string, n)		
	



#avoids("abcdefg", "zyxwuta")

def avoid_letters(string):
	for word in fin:
		avoids(word, string)
		


#avoid_letters("zyxwu") #this string of letters excludes only one word in the list.



# 9.4


def uses_only(string):

	n = 0

	def checker(word, string, n):
		if n < len(word):
			letter = word[n]
			if string.count(letter, 0, len(string)) != 0:
				n = n + 1
				checker(word, string, n)

			elif string.count(letter, 0, len(string)) == 0:
				return False

		else:
			print word
			return True
			
				
	def run(string, n):
		for word in fin:
			checker(word.strip(), string, n)


	run(string, n)


	

#uses_only("zyxwu")


