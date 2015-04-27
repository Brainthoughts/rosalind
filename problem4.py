__author__ = 'hannes'

a = 4300
b = 8487
mysum = 0

for x in range(a, b+1):
    if (x % 2 == 1):
        mysum += x

print(mysum)