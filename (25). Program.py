# Enter marks of 3 subjects from the user and store them in a dictionary
# Start with an empty dictionary and add one by one use subject name as key and marks as value

student={
}

physics=int(input("Enter Physics Marks :"))
computer=int(input("Enter Computer Marks :"))
english=int(input("Enter English Marks :"))

student.update({"Physics":physics})
student.update({"Computer":computer})
student.update({"English":english})

print(student)
