#
# Example file for working with o.s path module


import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

def main():


    # Get the modification time
    t = time.ctime(path.getmtime("guru99.txt.bak"))
    print(t)
    print(datetime.datetime.fromtimestamp(path.getmtime("guru99.txt.bak")))


if __name__ == "__main__":
    main()