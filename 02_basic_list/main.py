import random
import sys
import os

drink_list = ['Cola', 'Absolute', 'Sprite', 'Tercelar']

print('First Item is :', drink_list[0])

drink_list[0] = 'Juice'

print('First Item is :', drink_list[1:3])

other_events = ['event 1', 'event 6', 'event 3']

todos = [other_events,drink_list]

print(todos)

print((todos[1][1]))


drink_list.append('Venko')
print(drink_list)

drink_list.insert(1, "Sprinkle")
print(drink_list)

drink_list.remove("Sprinkle")
print(drink_list)

drink_list.sort()
print(drink_list)

drink_list.reverse()
print(drink_list)

del drink_list[2]
print(drink_list)

print(todos)

to_do_list2 = other_events + drink_list
print(to_do_list2)
print(len(to_do_list2))
print(max(to_do_list2))
print(min(to_do_list2))

