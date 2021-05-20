# prob16.py
import sys
import math

N = int(sys.argv[1])

with open("popular-names.txt","r") as file:
  txtlen = len(file.readlines())
  linesperfile = math.floor(txtlen/N)
  if txtlen % N != 0:
    linesperfile += 1
  linesleft = txtlen
file = open("popular-names.txt","r")
for i in range(N):
  filewrite_name = "popular-names-" + chr(ord('a')+i) + ".txt"
  filewrite = open(filewrite_name,"w")
  if linesleft >= linesperfile:
    linesleft -= linesperfile
    for j in range(linesperfile):
      filewrite.write(file.readline())
  else:
    for j in range(linesleft):
      filewrite.write(file.readline())
  filewrite.close()
file.close()