'''
Define a function that takes an integer argument and returns a logical value true or false depending on if the integer is a prime.

Per Wikipedia, a prime number ( or a prime ) is a natural number greater than 1 that has no positive divisors other than 1 and itself.
'''


def is_prime_new(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        print(i)
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def is_prime(n):
    if n < 2 or (n % 2 == 0 and n != 2) or (n % 3 == 0 and n != 3):
        return False
    for i in range(5, int(n**0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


print(is_prime_new(1816450723))
