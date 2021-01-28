# useful math function
import math
# help(math)

value = 4.35
print(math.floor(value))
print(math.ceil(value))
print(round(value))

# constants
print(math.pi)

from math import pi
print(pi)

print(math.e)
print(math.tau)
print(math.inf)
print(math.nan)

# Log Base e
print(math.log(math.e))
# print(math.log(0)) #value error
print(math.log(10))
print(math.e ** 2.302585092994046)

## math.log(x,base)
print(math.log(100,10))

print(math.sin(10))
print(math.degrees(pi/2))

import random
print(random.randint(0,100))

# The value 101 is completely arbitrary, you can pass in any number you want
random.seed(101)
# You can run this cell as many times as you want, it will always return the same number
print(random.randint(0,100))
print(random.randint(0,100))
print(random.randint(0,100))
print(random.randint(0,100))
print(random.randint(0,100))

# random with sequences
mylist = list(range(0,20))
print(mylist)
print(random.choice(mylist))
print(mylist)

# sample with replacement
print(random.choices(population=mylist,k=10))

# Shuffle a list
# Note: This effects the object in place!
# Don't assign this to anything!
print(random.shuffle(mylist))
print(mylist)

# Random distribution
# # Continuous, random picks a value between a and b, each value has equal change of being picked.
print(random.uniform(a=0,b=100))
print(random.gauss(mu=0,sigma=1))
