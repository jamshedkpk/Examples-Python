# Input a value and find odd or even
number=int(input("Enter A Value :"))
reminder=(number%2)
if(reminder==0):
    print("The Given No Is Even")
else:
    print("The Given No Is Odd")