'''
David Arce
Logan Lasiter
Assignment #3 - Parser
'''

import re

inputFile = open('in.txt', 'r')
outputFile = open('out.txt', 'w')

final = []
error_list = []
valid = {}
invalid = {}
v_key = 0
in_key = 0

def isOp(token):
	global error
	if token == '+' or token == '-' or token == '*' or token == '/' or token == '%':
		return True
	else:
		error_list.append("ERROR: Operator is not defined. A valid operator consists of '+', '-', '*', '/', '%'.")
		error = True
		return False

def isChar(token):
	if re.search('[a-zA-Z]', token):
		return True
	else:
		return False

def checkId(token):
	global error
	under_score = re.compile('_')
	char = re.compile('[a-zA-Z()]')
	idOk = re.compile('[a-zA-Z0-9_()]')
	if char.match(token, 0) or under_score.match(token, 0):
		for x in token:
			if not idOk.match(x):
				error_list.append("ERROR: Id is not of correct format. Id's consist of Chars, Digits & Underscores.")
				error = True
				return False
		return True
	else:
		error_list.append("ERROR: Id is not of correct format. Id's must begin with a Char or Underscore.")
		error = True
		return False

def isExpression(tokens):
	if checkId(tokens[0]) and isOp(tokens[1]) and checkId(tokens[2]) and len(tokens) > 4 and isOp(tokens[3]):
		final.append(tokens.pop(0)) # id
		final.append(tokens.pop(0)) # op
		isExpression(tokens)
		return True
	else:
		return False

'''
	If the statement is an 'Assignment', it will check for Id and '=',
	then will pop off tokens and append to new list "Final". Then, while
	there are still tokens, it will check for expression and add them to 
	new list "Final" if they are 'id op id' format.
'''
def checkAssignment(tokens):
	global error
	error = False
	if checkId(tokens[0]):
		if '=' in tokens:
			if ';' not in tokens:
				while len(tokens) != 0:
					final.append(tokens.pop(0))
				error_list.append("ERROR: Statement did not contain ';' to end the statement.")
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




# for every line in the in.txt, check if valid statement
for line in inputFile:
	tokens = line.split()
	checkAssignment(tokens)
	
	if not error:
		valid[v_key] = final
		v_key += 1
	else:
		invalid[in_key] = final
		in_key += 1

	final = []

outputFile.write('-- Good (Valid) Statements:\n\n')
for key, val in valid.items():
	outputFile.write(' '.join(val) + '\n')

outputFile.write('\n-- Bad (Invalid) Statements:\n\n')
i = 0
for key, val in invalid.items():
	outputFile.write(' '.join(val) + '\n')
	outputFile.write(error_list[i] + '\n')
	i += 1


inputFile.close()
outputFile.close()