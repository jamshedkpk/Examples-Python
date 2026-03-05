# Continue is used to skip any value in a loop

i=0
while (i<=10):
    if(i==5):
        i=i+1
        continue # To skip value 5    
    print(i)
    i=i+1
