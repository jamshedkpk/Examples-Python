# Set is a collection of un order items. In set duplicate value is
# Not returned

Collection={1,2,3,4,5,3,2,1,"data","ali",34.50}
print(Collection)
print(type(Collection))

myset=set() # To create new set
myset.add(1) # To add new value
myset.add((343,232,323,123)) # To add a new tuple in set
myset.add(2)
myset.add(3)
myset.remove(3) # To remove a value
# myset.clear() To clear set
myset.pop() # To remove any random value
print(myset)
set1={1,2,3,4,5}
set2={4,5,6,7,8}
print(set1.union(set2)) # Union of set1 & Set2
print(set1.intersection(set2)) # Intersection of set1 & set2