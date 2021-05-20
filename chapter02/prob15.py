# prob15.py
import sys

N = int(sys.argv[1])

file = open("popular-names.txt","r")
for line in file.readlines()[-N:]:
  print(line)
file.close()