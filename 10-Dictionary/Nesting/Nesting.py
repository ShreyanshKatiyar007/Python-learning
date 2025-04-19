# nested dictionary
student = {
    "name" : "shreyansh",
    "subject" : {
        "phy" : 98,
        "chem" : 99,
        "maths" : 95,
        "cs" : 99,
    }
}

print(student)

print(student["subject"]["cs"])
