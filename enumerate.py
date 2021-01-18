
lst = ['a','b','c']

for number,item in enumerate(lst):
    print(number)
    print(item)
# enumerate() becomes particularly useful when you have a case where you need to have some sort of tracker
for count,item in enumerate(lst):
    if count >= 2:
        break
    else:
        print(item)

# enumerate() takes an optional "start" argument to override the default value of zero
months = ['March','April','May','June']

print(list(enumerate(months,start=3)))