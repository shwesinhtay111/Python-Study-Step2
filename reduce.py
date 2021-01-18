from functools import reduce
lst = [47,11,42,13]
print(reduce(lambda x,y: x+y, lst))

from IPython.display import Image
print(Image('http://www.python-course.eu/images/reduce_diagram.png'))

#Find the maximum of a sequence (This already exists as max())
max_find = lambda a,b: a if (a > b) else b
#Find max
print(reduce(max_find,lst))