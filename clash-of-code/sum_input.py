import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
sum = 0
for i in range(n):
    op = input()
    sum += int(op)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(sum)
