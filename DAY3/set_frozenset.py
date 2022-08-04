"""set issubset()"""
#1
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
print(A.issubset(B))

#2
A = {'a', 'c', 'e'}
B = {'a', 'b', 'c', 'd', 'e'}
print('A is subset of B:', A.issubset(B))
print('B is subset of A:', B.issubset(A))

"""set symmetric_difference"""
#1
A = {'a', 'b', 'c', 'd'}
B = {'c', 'd', 'e'}
result = A.symmetric_difference(B)
print(result)

#2
A = {'python', 'java', 'c++'}
B = {'python', 'javascript', 'c'}
result = A.symmetric_difference(B)
print(result)

"""python frozenset() function"""
#1
mylist = ['black', 'white', 'red']
x = frozenset(mylist) 
print(mylist)
print(x)

#2
mylist =  ['apple', 'banana', 'cherry']
x = frozenset(mylist)
# x[1] = "strawberry"   ----> 'frozenset' object does not support item assignment
# print(x[1])

#3
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])
C = A.copy()
print(C)
print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
print(A.symmetric_difference(B))

#4
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])
C = frozenset([5, 6])
print(A.isdisjoint(C))
print(C.issubset(B))
print(B.issubset(C))

