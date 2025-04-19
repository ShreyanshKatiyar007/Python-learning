info = {
    "key" : "value",
    "name" : "alex",
    "age" : 19,
    "is_adult" : True,
    "learning" : ["python","C","java"],
    "topics" : ("dict","set"),
    "marks" : "95.93",
}
print(info)

print(type(info))

null_dict={}               # null dictionary
print(null_dict)

print(info["learning"])   # returns the value of given key

info["name"] = "Shreyansh"     # change the value of the given key
print(info)

info["surname"] = "Katiyar"    # create the new key-value pair
print(info)
