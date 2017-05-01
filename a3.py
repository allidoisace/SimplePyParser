'''
David Arce
Logan Lasiter

Assignment #3 - Parser
'''

import re

inputFile = open('in.txt', 'r')
outputFile = open('out.txt', 'w')

def isChar(token):
	# use RegEx here for chars and return True else False
	return True

def checkId(token):
	if isChar(token) or '_':
		return True
	else:
		return False


def checkAssignment(tokens):
	# will need to check if '(' or ')' are in tokens
	if checkId(tokens[0][0]):
		if '=' in tokens:
			print("This is an assignment.")
			# do next thing...the '=' will be the 2nd token so we can start at the 3rd token.
			# the 3rd token will HAVE to start with an id and develop an expression... id op id op id ...blah
		else:
			print("This is an expression.")
			# do next thing... id op id (we already know first id is there, go to op)
	else:
		print("Error with first Id...")




# for every line in the in.txt, check if valid statement
for line in inputFile:
	tokens = line.split()
	checkAssignment(tokens)
	# outputFile.write('Works\n')


inputFile.close()
outputFile.close()