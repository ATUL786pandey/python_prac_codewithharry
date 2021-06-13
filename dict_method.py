mydict = { "name":"Atul",
        "age":31,
        "last name" : "pandey",
        "friend":["Akshay","Shailendra","Tejas"],
        "grandfather" : {'father':'son'}
        }

#print(mydict.items())#it will return list inside tuple
#print(mydict.keys())
#print(mydict.values())
#mydict.update({"age":45})
#mydict.update({"friend":["manoj","suraj","pawan","nitin"]})
#mydict.update({"grandfather":{"father":"Atul"}})
print(mydict.get("name"))

print(mydict)