# Input 3 values and find greatest one
a=int(input("Enter A Value :"))
b=int(input("Enter A Value :"))
c=int(input("Enter A Value :"))
if(a>=b and a>=c):
    print("First Value Is Greater")
elif(b>=a and b>=c):    
    print("Second Value Is Greater")
elif(c>=a and c>=b):
    print("Third Value Is Greate")
else:
    print("Unkown Value Is Entered")