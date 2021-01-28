x = [1,3,4]
y = 2
z = 3

result = y + z
print(result)

# TypeError: unsupported operand type(s) for +: 'int' and 'list'
# result2 = y+x
# print(result2)

import pdb

x = [1,3,4]
y = 2
z = 3

result = y + z
print(result)

# Set a trace using Python Debugger
pdb.set_trace()
# error pdb
# result2 = y+x
# print(result2)