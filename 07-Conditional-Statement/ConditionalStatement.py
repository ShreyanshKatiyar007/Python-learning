light = "green"

if(light == "red"):
    print("stop")    # indentation

elif(light == "yellow"): # Only check if first statement is false.
    print("wait")

elif(light == "green"):
    print("go")

else:
    print("light is broken")    
