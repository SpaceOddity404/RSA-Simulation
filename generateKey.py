import math
import random

#extended euclidean algorithm outputs gcd, x coefficient, and y coefficient given parameters x and y
def extendedEuclidean(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x, y = extendedEuclidean(b%a, a)

    finx = y - (b//a) * x
    finy = x
    return gcd, finx, finy

#Generate two random distinct prime numbers p and q.
#For the purpose of this project, these numbers will not be as large as they would in a real scenario.

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
p = primes[random.randint(0, (len(primes) - 1))]
q = primes[random.randint(0, (len(primes) - 1))]
while p == q:
    q = primes[random.randint(0, (len(primes) - 1))]

#calculate n = pq and t = euler's totient function of n
n = p * q
t = (p - 1) * (q - 1)

#pick a random number e that is relatively prime to totient(n) such that 1 < e < totient(n)
e = random.randint(2, (t - 1))

while math.gcd(e, t) != 1:
    e = random.randint(2, t - 1)

#calculate the private key d using the extended euclidean algorithm
g, x, y = extendedEuclidean(e, t)
d = x
while d < 0:
    d += t






