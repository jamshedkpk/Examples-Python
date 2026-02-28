# Dictionary are used to store data in key:value form
# Dictionary in python is mutable for e.g changable

dictionary={
    "Name":"jamshed", 
    "Age":35,         
    "Subjects":["Python,Java,C++"], # Can store data in list 
    "Languages":("Urdu","English")  # Can store data in tuples
}

print(dictionary) # To print all data
print(dictionary["Age"]) # To print name only
dictionary["Name"]="Adnan" # To change data 
print(dictionary)
dictionary["Qualification"]="Mcs" # To assign new key:value
print(dictionary)

info={

} # Empty dictionary
info["Name"]="Salma" # Create new key:value in dictionary
print(info)