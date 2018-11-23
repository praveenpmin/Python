import os
from os import path

def main():
    # Print the name of the OS
    print(os.name)
#Check for item existence and type
print("Item exists:" + str(path.exists("guru99.txt")))
print("Item is a file: " + str(path.isfile("guru99.txt")))
print("Item is a directory: " + str(path.isdir("guru99.txt")))

if __name__ == "__main__":
    main()