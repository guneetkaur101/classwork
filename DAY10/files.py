f= open('another.txt','w')
f.write("hello welcome to my file!!")
f= open('another.txt')
text =f.read()
print(text)
f.close()