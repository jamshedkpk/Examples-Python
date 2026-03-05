# search any number in the list numbers=[1,4,9,16,25,36,49,64,81,100] 


numbers=[1,4,9,16,25,36,49,64,81,100]
num=int(input("Enter any number in the given list :"))
for i in numbers:
    if(i==num):
        print("Value found")
        break
    else:
        print("Not found")