David
Logan cssc1034

SimplePyParser

This program will take input from a text file, we used in.txt with this testing data:

first = one1 + two2 - three3 / four4 ;
second = one1 * (two2 * three3) ;
second = one1 * (two2 * three3) ;
third = ONE + twenty - three3 ;
third = old * thirty2 / b567 ;
one1 * i8766e98e + bignum
first = = one1 + two2 - three3 / four4 ;
first = one1 + two2 - three3 / four4
first = 1 + - two2 - three3 / four4 ;
first = one1 + two2 ? three3 / four4 ;
second = 4 + ( one1 * two2 ) * ( three3 + four4 ;
third = one1 + 24 - three3 ;
one1 +- delta
sixty6 / min = fourth ;

The output is the input text statements and whether or no they are valid or invalid and errors to describe why they are invalid:

-- Good (Valid) Statements:

first = one1 + two2 - three3 / four4 ;
second = one1 * (two2 * three3) ;
second = one1 * (two2 * three3) ;
third = ONE + twenty - three3 ;
third = old * thirty2 / b567 ;
one1 * i8766e98e + bignum

-- Bad (Invalid) Statements:

first = = one1 + two2 - three3 / four4 ;
ERROR: Id is not of correct format. Id's must begin with a Char or Underscore.
first = one1 + two2 - three3 / four4
ERROR: Statement did not contain ';' to end the statement.
first = 1 + - two2 - three3 / four4 ;
ERROR: Id is not of correct format. Id's must begin with a Char or Underscore.
first = one1 + two2 ? three3 / four4 ;
ERROR: Operator is not defined. A valid operator consists of '+', '-', '*', '/', '%'.
second = 4 + ( one1 * two2 ) * ( three3 + four4 ;
ERROR: Id is not of correct format. Id's must begin with a Char or Underscore.
third = one1 + 24 - three3 ;
ERROR: Id is not of correct format. Id's must begin with a Char or Underscore.
one1 +- delta
ERROR: Operator is not defined. A valid operator consists of '+', '-', '*', '/', '%'.
sixty6 / min = fourth ;
ERROR: Operator is not defined. A valid operator consists of '+', '-', '*', '/', '%'.



Grammar for valid statements (BNF):

<id> 			::= 	_|<char>|<id><char>|<id><digit>|<id>_

<digit> 		::= 	0|1|2|3|4|5|6|7|8|9

<char> 			::= 	a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|
 		   				y|z|A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|
 		   				W|X|Y|Z

<op>			::=		+|-|*|/|% 

<exp>			::=		id op id {op id}*

<assignment>	::=		id = exp ;

