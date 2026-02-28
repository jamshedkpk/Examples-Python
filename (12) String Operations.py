"""
A string is used to store data
In python a string is immutable for e.g 
It is not possible to change, add or delete its values 
"""
string1="This is a string of Python. \n It is used to store a sequance of data"
string2="This is a string of Python. \t It is used to store a sequance of data"
string3="Jamshed"
print(string1) # For new line
print(string2) # For tab
print(len(string3)) # For length of string
print(string3[0]) # For finding index 0 string
print(string3[1]) # For finding index 1 string 
print(string3[2]) # For finding index 2 string
print(string3[3]) # For finding index 3 string
print(string3[4]) # For finding index 4 string
print(string3[0:3]) # Slicing for finding string from 0 index to 3 index
print(string3.endswith("ed")) # Return true if it ends with ed
String4="apple"
String5=String4.capitalize() # For making capital of 1st letter of the string
print(String5)
print(String5.replace("pp","oo")) # For replacing pp in apple to oo
print(String5.find("pp")) # For finding pp index no
print(String5.count("p")) # For counting p in the string
print("I am a string " + "I am new string") # String concatenation