#while loop
count = 0
while (count < 9):
   print ('The count is:', count)
   count = count + 1

# for loop
for letter in 'Python':    
   print ('Current Letter :', letter)

for x in range (10):
     for y in range (11,15):
       print (x,y)

# Use of break and continue keyboard
print("use of break keyword")
num = 0
for i in range(10):
	num += 1
	if num == 8:
		break
	print("The num has value:", num)
print("Out of loop")


# continue
print("use of continue keyword")
for i in range(1, 11):
	if i == 6:
		continue
	else:
		print(i, end=" ")