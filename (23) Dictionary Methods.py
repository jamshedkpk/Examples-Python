Info={
    "Name":"Jamshed",
    "Age":35,
    "Marks":780
}
print(Info.keys()) # To get all keys in dictionary
print(Info.values()) # To get all values in dictionary
print(Info.items()) # To get all keys and values in the form of tuples
print(Info.get("Age")) # To get age key value in dictionary
Info.update({"City":"Lakki Marwat"}) # To add new key pair value in dictionary
print(Info)