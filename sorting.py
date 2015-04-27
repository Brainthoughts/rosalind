__author__ = 'hannes'


def compare(a, b):
    if a < b:
        return 1
    elif a > b:
        return -1
    else:
        return 0


def sort(l):
    iterations = 0
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            c = compare(l[i], l[j])
            if c < 0:
                v = l[i]
                l[i] = l[j]
                l[j] = v
            iterations += 1
    print("For list size ", len(l), iterations, "iterations run")
    return l


def sort3(l):
    iterations = 0
    for index in range(1, len(l)):
        value = l[index]
        i = index - 1
        while i >= 0 and value < l[i]:
            l[i + 1] = l[i]
            l[i] = value
            i -= 1
        iterations += 1
    print("For list size ", len(l), iterations, "iterations run")
    return l


myList = [4, 8, 6, 2, 5, 1, 7, 3]
print(myList)
print(sort(myList))
myList = [4, 8, 6, 2, 5, 1, 7, 3]
print(sort3(myList))
an = ['c', 'd', 'a', 'b']
print(an)
print(sort(an))
an = ['c', 'd', 'a', 'b']
print(sort3(an))
