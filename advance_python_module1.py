############# Counter ###########
# Counter is a dict subclass which helps count hashable objects. Inside of it elements are stored as dictionary keys and the counts of the objects are stored as the value.
from collections import Counter
lst = [1,2,2,2,2,3,3,3,1,2,1,12,3,2,32,1,21,1,223,1]
print(Counter(lst))
print(Counter('aabsbsbsbhshhbbsbs'))
s = 'How many times does each word show up in this sentence word times each each word'
words = s.split()
print(Counter(words))
# Methods with Counter()
c = Counter(words)
print(c.most_common(2))

############# defaultdict ###########
# defaultdict is a dictionary-like object which provides all methods provided by a dictionary but takes a first argument (default_factory) as a default data type for the dictionary. Using defaultdict is faster than doing the same using dict.set_default method.
# A defaultdict will never raise a KeyError. Any key that does not exist gets the value returned by the default factory.

from collections import defaultdict
d = {}
# keyError not using defaultdict
# print(d['one'] )

d  = defaultdict(object)
print(d['one'] )
for item in d:
    print(item)

# initialize with default values
d = defaultdict(lambda: 0)
print(d['one'] )

############ namedtuple ###########
# standard tuple uses numerical indexes to access its members
t = (12,13,14)
print(t[0])
#  remembering which index should be used for each value can lead to errors, especially if the tuple has a lot of fields and is constructed far from where it is used
# A namedtuple assigns names, as well as the numerical index, to each member
from collections import namedtuple
#  construct the namedtuple by first passing the object type name (Dog) and then passing a string with the variety of fields as a string with spaces between the field names
Dog = namedtuple('Dog',['age','breed','name'])
sam = Dog(age=2,breed='Lab',name='Sammy')
frank = Dog(age=2,breed='Shepard',name="Frankie")
print(sam)
print(frank)
