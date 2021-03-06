'''
Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. The first ten pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 − 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal
and D = |Pk − Pj| is minimised; what is the value of D?
'''

def Pentagon (a):
    if (1+(24*a+1)**0.5) % 6 == 0:
        return True
    return False

test = True

i = 1
while test == True:
    for j in range(1, i):
        m = i*(3*i-1)/2
        n = j*(3*j-1)/2

        if Pentagon(n+m) and Pentagon(m-n):
            print(m-n)
            test = False
    i += 1
