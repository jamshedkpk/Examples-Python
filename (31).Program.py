# Find any value in the list [1,4,9,16,25,36,49,64,81,100] by using while loop

numbers=(1,4,9,16,25,36,49,64,81,100)
x=36
i=0 # Initialization
while(i<len(numbers)): # length of list
    if(numbers[i]==x):
            print("Value is found at index :", i)
    i+=1
        