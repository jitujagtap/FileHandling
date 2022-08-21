#WAP to take input from user and print the entered number of lines
num = int(input("enter the number of lines you need to read : "))
#f = open("C:/Users/hunny/OneDrive/Desktop/hello.txt","r+")
"""Solution 1"""
with open("C:/Users/hunny/OneDrive/Desktop/hello.txt","r") as f:
    for i in range(num):
        print(f.readline)

"""Solution 2"""
lines = f.readlines()
newLines = lines[0:num]

for line in newLines:
    print(line)