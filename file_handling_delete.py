import os

if os.path.exists("C:/Users/hunny/OneDrive/Desktop/hello.txt"):
    os.remove("C:/Users/hunny/OneDrive/Desktop/hello.txt")
    print("hello.txt file is removed")
else:
    print("File does not exist on the path")

""" code for the rename file"""
