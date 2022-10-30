# isPrime() function determine prime and non prime by outputing boolean (True/False)
def isPrime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

# primes variable is to receive all primes from ListAllPrimes function
primes=[]
#ListPrimeUntil is a variable that output all primes from 2< prime number<ListPrimeUntil
def ListAllPrimes(ListPrimeUntil):
    for j in range(2,ListPrimeUntil):
        if isPrime(j)==True:
            primes.append(j)

# HugeNumber variable receive the number to be tested
def TestHugeNumber(HugeNumber):
    for prime in primes:
        if HugeNumber%prime==0:
            return False
    return True