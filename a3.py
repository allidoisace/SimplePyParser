'''
David Arce cssc0858
Logan Lasiter cssc1034

CS 530 Assignment #3 - Parser

Execution:
Run the program by typing in cmd of program directory:
(Edoras has python 3.6 & 2.7 installed: http://edoras.sdsu.edu/software/)
	With ONLY Python 3 installed:
		python a3.py
	With Python 2 & 3 installed:
		python3 a3.py
The execution will output valid and invalid statements and their errors in the out.txt file.


This program will take input from a text file in.txt
'''

import re

# File Streams
inputFile = open('in.txt', 'r')
outputFile = open('out.txt', 'w')

# Global Vars
final = []
error_list = []
valid = {}
invalid = {}
v_key = 0
in_key = 0

# Takes in a token and checks if it is an operator described in the BNF ruleset.
def isOp(token):
	global error
	if token == '+' or token == '-' or token == '*' or token == '/' or token == '%':
		return True
	else:
		error_list.append("ERROR with Operator ' " + str(token) + " ' incorrect operator. A valid operator consists of '+', '-', '*', '/', '%'.")
		error = True
		return False

# Takes in a token and checks if it is a char.
def isChar(token):
	if re.search('[a-zA-Z]', token):
		return True
	else:
		return False

# Takes in a token and checks if it is of correct format labelled in the BNF ruleset.
def checkId(token):
	global error
	under_score = re.compile('_')
	char = re.compile('[a-zA-Z()]')
	idOk = re.compile('[a-zA-Z0-9_()]')
	if char.match(token, 0) or under_score.match(token, 0):
		for x in token:
			if not idOk.match(x):
				error_list.append("ERROR with Id ' " + str(token) + " ' incorrect format. Id's consist of Chars, Digits & Underscores.")
				error = True
				return False
		return True
	else:
		error_list.append("ERROR with Id ' " + str(token) + " ' incorrect format. Id's must begin with a Char or Underscore.")
		error = True
		return False

# Takes tokens from statement and checks if correct format and is called recursively till end of statement or an error.
def isExpression(tokens):
	if checkId(tokens[0]) and isOp(tokens[1]) and checkId(tokens[2]) and len(tokens) > 4 and isOp(tokens[3]):
		final.append(tokens.pop(0)) # id
		final.append(tokens.pop(0)) # op
		isExpression(tokens)
		return True
	else:
		return False
'''
	Takes tokens from each statement and checks if it is an assignment or expression. Also identifies if the statement
	is valid or invalid.
'''
def checkAssignment(tokens):
	global error
	error = False
	if checkId(tokens[0]):
		if '=' in tokens:
			if ';' not in tokens:
				while len(tokens) != 0:
					final.append(tokens.pop(0))
				error_list.append("ERROR with Statement, incorrect format. did not contain ';' to end the statement.")
				error = True
			else:
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
						while len(tokens) != 0:
							final.append(tokens.pop(0))
						break
		else:
			while len(tokens) != 0:
				if isExpression(tokens):
					final.append(tokens.pop(0)) # id
					final.append(tokens.pop(0)) # op
					final.append(tokens.pop(0)) # id
				else:
					while len(tokens) != 0:
						final.append(tokens.pop(0))
					break




# for every line in the in.txt, check if valid statement and store in dictionary for output.
for line in inputFile:
	tokens = line.split()
	if line in ['\n', '\r\n']:
		continue
	checkAssignment(tokens)
	
	if not error:
		valid[v_key] = final
		v_key += 1
	else:
		invalid[in_key] = final
		in_key += 1

	final = []

# for every valid statement, output to file.
outputFile.write('-- Good (Valid) Statements:\n\n')
for key, val in valid.items():
	outputFile.write(' '.join(val) + '\n')

# for every invalid statement, output to file with error.
outputFile.write('\n-- Bad (Invalid) Statements:\n\n')
i = 0
for key, val in invalid.items():
	outputFile.write(' '.join(val) + '\n')
	outputFile.write(error_list[i] + '\n')
	i += 1


inputFile.close()
outputFile.close()