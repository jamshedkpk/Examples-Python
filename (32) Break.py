# Break is a keyword used for stop the loop to a specific point

numbers=(1,4,9,16,25,36,49,64,81,100)
x=36
i=0 
while(i<len(numbers)):
    if(numbers[i]==x):
            print("Value is found at index :", i)
            break # To stop the loop at index 5
    else:
        print("Value is not found at index :", i)
    i+=1
