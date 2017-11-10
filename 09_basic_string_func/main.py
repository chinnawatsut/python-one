import os
import sys

long_string = "I'll cath you if     d you fall"
print(long_string[0:4])

print(long_string[-5:])

print(long_string[:-5])

print(long_string[:4] + " be there")

print("%c is my %s letter and my number %d number is %.5f" %('X', 'favorite',1,.14))

print(long_string.capitalize())
print(long_string.find("you"))
print(long_string.isalnum())
print(len(long_string))
print(long_string.replace("fall","flop"))
print(long_string.strip())

quoute_list = long_string.split(" ")
print(quoute_list)