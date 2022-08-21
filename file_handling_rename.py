import os
""" code for the rename file"""
if os.path.exists("C:/Users/hunny/OneDrive/Desktop/hello.txt"):
    os.rename("C:/Users/hunny/OneDrive/Desktop/hello.txt","C:/Users/hunny/OneDrive/Desktop/emailFormat.txt")
    print("hello.txt file is renamed")
else:
    print("File does not exist on the path")


