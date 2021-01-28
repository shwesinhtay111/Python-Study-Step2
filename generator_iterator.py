# Generator function for the cube of numbers (power of 3)
def gencubes(n):
    for num in range(n):
        yield num**3
for x in gencubes(10):
    print(x)

def genfibon(n):
    """
    Generate a fibonnaci sequence up to n
    """
    a = 1
    b = 1
    for i in range(n):
        yield a
        a,b = b,a+b
for num in genfibon(10):
    print(num)

# Normal Function
def fibon(n):
    a = 1
    b = 1
    output = []
        
    for i in range(n):
        output.append(a)
        a,b = b,a+b
            
    return output
fibon(10)

# next() and iter() built-in functions
def simple_gen():
    for x in range(3):
        yield x
# Assign simple_gen 
g = simple_gen()

print(next(g))
print(next(g))
print(next(g))

# After yielding all the values next() caused a StopIteration error
# You might be wondering that why don’t we get this error while using a for loop? A for loop automatically catches this error and stops calling next().
# print(next(g))

s = 'hello'

#Iterate over string
for let in s:
    print(let)
# But that doesn't mean the string itself is an iterator! We can check this with the next() function:error occurs!
# next(s)

# a string object supports iteration, but we can not directly iterate over it as we could with a generator function. The iter() function allows us to do just that!
s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
# Error hello finished out
# print(next(s_iter))

#  yield keyword at a function will cause the function to become a generator. This change can save you a lot of memory for large use cases