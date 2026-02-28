""" 
Tople is used to store multiple data inside a single variable
Like a list but list is mutable while a tople is immutable like a string
We can't change, add or delete its values
It can store different data types
"""
fruits=("Banana", "Apple", "Orange",540)
print(fruits)
print(fruits[0]) # Print value at index 0
print(fruits[0:2]) # Slicing in tuples to access value from index 0 to 2
print(fruits.count("Banana")) # Count Banana in fruits