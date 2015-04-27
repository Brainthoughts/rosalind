__author__ = 'hannes'

f = open('test.txt', 'r')
line_nr = 0

for line in f:
    line_nr += 1
    if (line_nr % 2 == 0):
        print(line, end="")