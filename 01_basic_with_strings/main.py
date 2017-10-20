import random
import sys
import os

#run files : python file.py

'''
Variable types
  - Numbers
  - Strings
  - Lists
  - Tuples
  - Dictionaries
Operators
  + - * / % ** //

'''

name = "Cygik"
print("Hello "+name)

'''
print ' 5 + 2 = ', 5+2
print ' 5 - 2 = ', 5 -2
print ' 5 * 2 = ', 5 *2
print ' 5 / 2 = ', 5 /2
print ' 5 % 2 = ', 5 %2
print ' 5 ** 2 = ' , 5 **2
print ' 5 // 2 = ' , 5 //2
'''
quote = "\"Always remmeber you are unique"

multi_line_quote = ''' just
like everyone else'''

print("%s %s %s" %('I like the quite', quote,multi_line_quote))

print('\n' * 5)
print("I don't like ", end="")
print("newlines")