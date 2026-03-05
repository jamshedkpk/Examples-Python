# WAP to input a number and check if the number is even or odd
# By using a funtion

def check_even_odd(n):
    reminder=(n%2)
    if(reminder==0):
        print("The given no is even")
    else:
        print("The given no is odd")
    
n=int(input("Enter a no : "))
check_even_odd(n)