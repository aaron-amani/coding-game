import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

num = int(input())
path = ""
for i in range(num):
    folder = input()
    path += folder + '/'

filename = input()
extension = input()
path += filename + '.' + extension



# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(path)
