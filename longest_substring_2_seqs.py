__author__ = 'hannes'

"""
Given: Two DNA strings s and t (each of length at most 1 kbp).

Return: All locations of t as a substring of s.
"""

def long_substr(data):
    substr = ''
    if len(data) > 1 and len(data[0]) > 0:
        for i in range(len(data[0])):
            for j in range(len(data[0])-i+1):
                if j > len(substr) and is_substr(data[0][i:i+j], data):
                    substr = data[0][i:i+j]
    return substr

def is_substr(find, data):
    if len(data) < 1 and len(find) < 1:
        return False
    for i in range(len(data)):
        if find not in data[i]:
            return False
    return True


input = """
GATATATGCATATACTT
ATAT
"""
data = input.strip().split("\n")

print(long_substr(data))