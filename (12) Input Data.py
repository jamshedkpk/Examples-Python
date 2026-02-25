"""
It must be remember to you that whenever submit any data throug input
Then python understand it as a string weither it is an integer or float
"""
name=input("Enter Your Name :")
age=int(input("Enter Your Age :"))
marks=float(input("Enter Your Marks :"))

print(type(name),name)
print(type(age),age)
print(type(marks),marks)