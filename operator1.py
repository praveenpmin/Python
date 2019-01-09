import sys, glob, operator
sys.argv = reduce(operator.add, map(glob.glob, sys.argv))
print (sys.argv)