mylist = ["Apple", "Banana", "Carrot", "Durian"]
my_dict = {
    "name": "Gavin",
    "age": 40
}

for item in mylist:
    print(item)
    
print(my_dict["name"])

for key in my_dict:
    print(key, ":", my_dict[key])