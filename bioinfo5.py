__author__ = 'hannes'


def mortal_fib(n, l, k=1, m=1):
    """
    Return the mortal fibbonacci table for n months and k pari of
    rabbits in each reproduction.

    l = life time of the rabbits
    m = maturity time
    """
    fib_table = []
    for i in range(n):
        if i < l:
            if i < 2:
                fib_table.append(1)
            else:
                fib_table.append(fib_table[-1] + fib_table[-2] * k)
        else:
            rabbits = 0
            for j in range(i - l, i - m):
                rabbits += fib_table[j] * k
            fib_table.append(rabbits)
    return fib_table


n = 84
k = 1
l = 20
m = 1
print(mortal_fib(n, l, k, m)[-1])