__author__ = 'hannes'

f = open('bioinfo7.txt', 'r')
s1, s2 = f.read().split("\n")
hd = 0;

for i in range(0,len(s1)):
    if s1[i] != s2[i]:
        hd += 1


print(hd)