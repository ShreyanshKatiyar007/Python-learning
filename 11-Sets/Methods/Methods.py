set = {1}

set.add(2)            # adds an element
set.add(3)
set.add("hello")
print(set)

set.remove(1)         # removes the element
print(set)

print(set.pop())      # remove a random value
print(set)

set.clear()           # empties the set
print(len(set)) 

set1 = {1,2,3}
set2 = {2,3,4,5}

print(set1.union(set2))    # combines both set values and return new 

print(set1.intersection(set2))    # combines common values and returns new
