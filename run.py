#import solution.py file to accsess the functions such as 
# isPrime(),ListAllPrimes(),TestHugeNumber()
import solution 

# n variable let user enter a number
n=int(input("Enter the number > :"))
# call ListAllPrimes() function from solution.py
solution.ListAllPrimes(n)

# testing the variable n to decide if n  is a prime number
if solution.TestHugeNumber(n)==True:
    print(n,"is Prime Number")
else:
    print(n,"is not Prime Number")
