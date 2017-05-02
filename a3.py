'''
David Arce
Logan Lasiter
Assignment #3 - Parser
'''

import re

inputFile = open('in.txt', 'r')
outputFile = open('out.txt', 'w')

final = []
valid = {}
invalid = {}
isValid = True
v_key = 0
in_key = 0

def isOp(token):
	# could just use else if's or dict or regex to test for op.
	if token == '+' or token == '-' or token == '*' or token == '/' or token == '%':
		return True
	else:
		return False

def isChar(token):
	# use RegEx here for chars and return True else False
	if re.search('[a-zA-Z]', token):
		return True
	else:
		return False

def checkId(token):
	under_score = re.compile('_')
	char = re.compile('[a-zA-Z]')
	idOk = re.compile('[a-zA-Z0-9_]')
	if char.match(token, 0) or under_score.match(token, 0):
		if idOk.match(token):
			print('this is an ID.')
			return True
		else:
			return False
	else:
		return False

def isExpression(tokens):
	if checkId(tokens[0]) and isOp(tokens[1]) and checkId(tokens[2]) and len(tokens) > 4 and isOp(tokens[3]):
		final.append(tokens.pop(0)) # id
		final.append(tokens.pop(0)) # op
		isExpression(tokens)
		# elif ';' in tokens:
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
	# will need to check if '(' or ')' are in tokens
	print(tokens)
	if checkId(tokens[0][0]):
		if '=' in tokens:
			print("This is an assignment.")
			if ';' not in tokens:
				print("Invalid Statement...")
				while len(tokens) != 0:
					final.append(tokens.pop(0))
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
						print("Invalid Statement...")
						while len(tokens) != 0:
							final.append(tokens.pop(0))
						break

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
					while len(tokens) != 0:
						final.append(tokens.pop(0))
					break
			# do next thing... id op id (we already know first id is there, go to op)
	else:
		print("Error with first Id...")




# for every line in the in.txt, check if valid statement
for line in inputFile:
	tokens = line.split()
	checkAssignment(tokens)
	# outputFile.write('Works\n')
	print(final)
	
# 	if isValid:
# 		valid[v_key] = final
# 		v_key += 1
# 	else:
# 		invalid[in_key] = final
# 		in_key += 1

# 	final = []

# for key, val in valid:
# 	print('\n'.join(str(val) for val in myList))


inputFile.close()
outputFile.close()