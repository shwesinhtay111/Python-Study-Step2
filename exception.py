try:
    f = open('testfile','w')
    f.write('Test write this')
except IOError:
    print('Error: Could not fine file or read data')
else:
    print('Content written successfully')
    f.close()

try:
    f = open('testfile','r')
    f.write('Test write this')
except IOError:
    # This will only check for an IOError exception and then execute this print statement
    print("Error: Could not find file or read data")
else:
    print("Content written successfully")
    f.close()

try:
    f = open('testfile','r')
    f.write('Test write this')
except:
    # This will check for any exception and then execute this print statement
    print("Error: Could not find file or read data")
else:
    print("Content written successfully")
    f.close()

# finally: block of code will always be run regardless if there was an exception in the try code block
try:
    f = open("testfile", "w")
    f.write("Test write statement")
    f.close()
finally:
    print("Always execute finally code blocks")

def askint():
    try:
        val = int(input('Please enter an interger: '))
        print(val)
    except:
        print('Looks like you did not enter interger')
    finally:
        print('Finally, You excuted!')
askint()
def askint():
    while True:
        try:
            val = int(input("Please enter an integer: "))
        except:
            print("Looks like you did not enter an integer!")
            continue
        else:
            print("Yep that's an integer!")
            break
        finally:
            print("Finally, I executed!")
        print(val)
askint()