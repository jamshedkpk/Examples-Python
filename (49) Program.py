# WAP to print factorial of a number by using function

def print_factorial(n):
    i=1
    fact=1
    while(i<=n):
        fact=fact*i
        i=i+1
        print(fact)


print_factorial(5)