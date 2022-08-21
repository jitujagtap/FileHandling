#WAP to take input from user and print the entered number of lines from end of the file
num = int(input("enter the number of lines you need to read : "))
f = open("C:/Users/hunny/OneDrive/Desktop/hello.txt","r+")
#with open("C:/Users/hunny/OneDrive/Desktop/hello.txt","r") as f:
lines = f.readlines()
newLines = lines[::-1]
for line in newLines[0:num]:
    print(line)