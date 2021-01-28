s = 'Global Variable'
def check_for_locals():
    print(locals())
print(globals())

print(globals().keys())

print(globals()['s'])

check_for_locals()

def hello(name='Jose'):
    return 'Hello' + name
print(hello())

greet = hello
print(greet())
 
# del hello
# print(hello())
# print(greet())
def hello11(name='Jose'):
    print('The hello() function has been executed')
        
    def greet():
        return '\t This is inside the greet() function'
        
    def welcome():
        return "\t This is inside the welcome() function"
        
    print(greet())
    print(welcome())
    print("Now we are back inside the hello() function")

hello11()

def hellotest(name='Jose'):
    
    def greet():
        return '\t This is inside the greet() function'
        
    def welcome():
        return "\t This is inside the welcome() function"
        
    if name == 'Jose':
        return greet
    else:
        return welcome
x = hellotest()
print(x())

def new_decorator(func):

    def wrap_func():
        print("Code would be here, before executing the func")

        func()

        print("Code here will execute after the func()")

    return wrap_func

def func_needs_decorator():
    print("This function is in need of a Decorator")

func_needs_decorator()

func_needs_decorator = new_decorator(func_needs_decorator)
func_needs_decorator()

@new_decorator
def func_needs_decorators():
    print("This function is in need of a Decorator")
func_needs_decorators()