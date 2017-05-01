'''
David Arce
Logan Lasiter

Assignment #3 - Parser
'''

import re

inputFile = open('in.txt', 'r')
outputFile = open('out.txt', 'w')

final = []

def isOp(token):
	# could just use else if's or dict or regex to test for op.
	return True

def isChar(token):
	# use RegEx here for chars and return True else False
	return True

def checkId(token):
	if isChar(token) or '_':
		return True
	else:
		return False

def isExpression(tokens):
	if tokens[1] == ';':
		final.append(tokens.pop(0)) # id
		print(tokens)
		return False
	elif checkId(tokens[0]):
		if isOp(tokens[1]):
			print(tokens)
			if checkId(tokens[2]):
				if len(tokens) > 3:
					if isOp(tokens[3]):
						final.append(tokens.pop(0)) # id
						final.append(tokens.pop(0)) # op
						isExpression(tokens)
					else:
						print("Something WRONG!")
					return True
				else: 
					return True
			else:
				return False
		else:
			return False
	else:
		return False
		

'''
	If the statement is an 'Assignment', it will check for Id and '=',
	then will pop off tokens and append to new list "Final". Then, while
	there are still tokens, it will check for expression and add them to 
	new list "Final" if they are 'id op id' format.
'''
def checkAssignment(tokens):
	# will need to check if '(' or ')' are in tokens
	if checkId(tokens[0][0]):
		if '=' in tokens:
			print("This is an assignment.")
			final.append(tokens.pop(0)) # id
			final.append(tokens.pop(0)) # '='
			while len(tokens) != 0:
				if tokens[0] == ';':
					final.append(tokens.pop(0)) # ';'
				elif isExpression(tokens):
					final.append(tokens.pop(0)) # id
					final.append(tokens.pop(0)) # op
					final.append(tokens.pop(0)) # id
				else:
					print("Invalid Statement...")

			# do next thing...the '=' will be the 2nd token so we can start at the 3rd token.
			# the 3rd token will HAVE to start with an id and develop an expression... id op id op id ...blah
		else:
			print("This is an expression.")
			while len(tokens) != 0:
				if isExpression(tokens):
					final.append(tokens.pop(0)) # id
					final.append(tokens.pop(0)) # op
					final.append(tokens.pop(0)) # id
				else:
					print("Invalid Statement...")
			# do next thing... id op id (we already know first id is there, go to op)
	else:
		print("Error with first Id...")




# for every line in the in.txt, check if valid statement
for line in inputFile:
	tokens = line.split()
	checkAssignment(tokens)
	# outputFile.write('Works\n')
	print(final)


inputFile.close()
outputFile.close()