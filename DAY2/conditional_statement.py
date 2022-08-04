"""Conditional statements"""
#1
a = 15
b = 4
if (a>b):
    print("hello")

#2
a = 15
b = 140
if (a > b):
    print("hello")
else:
    print("hi")

#3
b = 40
c = 45
if(b>c):
    print('b is greater than c')
else:
    print('b is not greater than c')

#4
a = 140
b = 20
c = 64
if(b>c):
    print( b ,'is greater than ',c)
elif(a>c):
    print( a ,'is greater than ',c)
elif(b==c):
    print( b ,'is equal to ',c)

"""identity operator"""
a = 10
b = 10
print(a is b)           #is operation
print(a is not b)       #is not operation
a = 10 
b = 20
print(a is b)           #is operation
print(a is not b)       #is not operation


"""Membership operator"""
x = ["apple", "banana"]
print("banana" in x)            #Membership in operator
print("banana" not in x)        #Membership not in operator

x = ["5", "9"]
print("9" in x)                 #Membership in operator
print("9" not in x)             #Membership not in operator





