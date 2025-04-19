student = {
    "name" : "shreyansh",
    "subjects" : {
      "phy" : 98,
      "chem" : 96,
      "maths" : 95,
      "cs" : 99
    }
}

print(student.keys())      # return all keys

print(student.values())    # return all values

print(student.items())     # return all items as tuples

pairs = list(student.items())  
print(pairs[0])            # return the item value at given index

print(student.get("name")) # return the value according to the key

student.update({"city" : "delhi"})
print(student)             # insert the specified items to the dictionary
