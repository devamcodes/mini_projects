"""
project: practicing generators.
"""


def thousand_numbers():
    i = 0
    while i <1000:
        yield i
        i +=1



g = thousand_numbers()
print(next(g))


object = range(4)
print(object)


def prime_numbers_in_thousand():
    for n in range(2,10):
        for x in range(2,n):
            if n % x == 1:
                print("This is a composite number")

        else:
            yield n


g1 = prime_numbers_in_thousand()
print(list(g1))