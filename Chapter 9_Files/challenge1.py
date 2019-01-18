import os
mypath = os.path.join("c:/", "sourcedir")

with open("hello.txt", "r") as f:
    print(f.read())