# prob14.txt
import sys

N = int(sys.argv[1])

file = open("popular-names.txt","r")
for i in range(N):
    print(file.readline())
file.close()