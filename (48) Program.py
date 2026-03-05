# WAP to print the elements of a list in a single line seperating them by -  by using a function and for loop

def align_list(cities):
    for city in cities:
        print(city, end="-")
    
    
cities=["Karachi","Peshawar","Islamabad","Lahore","Multan"]
align_list(cities)