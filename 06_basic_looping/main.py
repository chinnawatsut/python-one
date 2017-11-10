import sys
import os
import random

for x in range(0,10):
    print(x, ' ' ,end='')
print('\n')

grocery_list = ['EVa','Molloc','Hawk']

for y in grocery_list:
    print(y)

for x in [2,4,6,8,10]:
    print(x)

num_list = [[1,2,3],[10,20,30],[100,200,300]]

for l in num_list:
    for h in l:
        print(h,' ', end='')

#While Loop

random_num = random.randrange(0,100)

while(random_num != 15):
    print(random_num)
    random_num = random.randrange(0,100)

i = 0;

while(i <= 20):
    if(i%2 == 0):
        print(i)
    elif (i == 9):
        break
    else:
        i += 1
        continue
    i += 1