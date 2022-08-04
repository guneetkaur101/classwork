my_list = ['p', 'y', 't', 'h', 'o','n']

print(my_list[0])  

print(my_list[2])  

print(my_list[4]) 

# List slicing in Python

my_list = ['p','r','o','g','r','a','m']

print(my_list[2:5])

# Appending and Extending lists in Python
l1 = [1, 3, 5]

l1.append(7)

print(l1)

l1.extend([9, 11, 13])

print(l1)

list = ["book", "copy", "pen"]
if "apple" in list:
    print("yes, apple in list")

"""CHANGE ITEM"""
#1
list = ["black", "white", "red", "blue", "yellow"]
list[1] = "pink"
print(list)

#2
list = ["black", "white", "red", "blue", "yellow"]
list[1:4] = "green", "orange"
print(list)

#3
list = ["black", "white", "red", "blue", "yellow"]
list[0:5] = "green", "orange"
print(list)

#4
list = ["black", "white", "red", "blue", "yellow"]
list[1:3] = "green", "orange"
print(list)

"""INSERT ITEM"""
#1
list = ["black", "white", "red", "blue", "yellow"]
list.insert(2, "green")
print(list)

list = ["black", "white", "red", "blue", "yellow"]
list.insert(2, "green")
list.insert(4, "orange")
print(list)

list = ["black", "white", "red", "blue", "yellow"]
list.insert(0, "pink")
list.insert(6, "purple")
print(list)


#EXTEND LIST (Add the elements of tropical to list)
list1 = ["black", "blue", "brown"]
list2 = ["white", "sky", "red"]
list.extend(list2)
print(list1)

l = [1,2,3]
n = int(input("enter the no. of elements in the list: "))
for x in range(0,2):
    l.append(input("enter the item: "))
print("printing the list item: ")
for x in l:
    print(x, end = " ")

"""REMOVE LIST ITEM"""
list = ["yellow", "red", "black", "orange"]
list.remove("black")
print(list)

list = ["yellow", "red", "black", "orange"]
list.pop(2)
print(list)

list = ["yellow", "red", "black", "orange"]
list.pop()
print(list)

list = ["yellow", "red", "black", "orange"]
del list[0]
print(list)

list = ["yellow", "red", "black", "orange"]
del list[3]
print(list)

list = ["yellow", "red", "black", "orange"]
del list[0:2]
print(list)

list = ["yellow", "red", "black", "orange"]
del list[2:3]
print(list)

list = ["yellow", "red", "black", "orange"]
del list[0:3]
print(list)
