# Logical operators are used to combine multiple conditions

# And operator return the result true if both conditions are true
name="Jamshed"
loginid="yes"
if(name=="Jamshed") and (loginid=="yes"):
    print("Welcome To Your Dashboard")

# Or operator return the result true if one condition are true
name="Jamshed"
marks=800
if(name=="Jamshed") or (marks>=800):
    print("You are passed")

# not operator reverse the result
raining=False
if(not (raining)) :
    print("Please go outside for a walk")
