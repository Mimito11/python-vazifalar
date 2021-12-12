# thisset = {"apple", "banana", "cherry"}
# thisset.add("orange")
# print(thisset)

# thisset = {"apple", "banana", "cherry", "apple", }
# tropical = {"pineapple", "mango", "papaya"}

# thisset.update(tropical)
# print(len(thisset))
# print(thisset)
# print(type(thisset))




# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = set1.union(set2)
# print(set3)

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set1.update(set2)
# print(set1)




# x = {"apple", "banana", "cherry"}
# y = {"goole", "microsoft", "apple", "cherry"}
# x.intersection_update(y)
# print(x)

# x = {"apple", "banana", "cherry"}
# y = {"goole", "microsoft", "apple"}
# z = x.intersection(y)
# print(z)




# x = {"apple", "banana", "cherry"}
# y = {"goole", "microsoft", "apple"}
# x.symmetric_difference_update(y)
# print(x)

# x = {"apple", "banana", "cherry"}
# y = {"goole", "microsoft", "apple"}
# z = x.symmetric_difference(y)
# print(z)




# thisdict = {
#     "brand": "ford",
#     "model": "mustang",
#     "year": 1964
# }
# print(thisdict)

# thisdict = {
#     "brand": "ford",
#     "model": "mustang",
#     "year": 1964
# }
# print(thisdict["brand"])




# thisdict = {
#     "brand": "ford",
#     "model": "mustang",
#     "year": 1964
# }
# x = thisdict["model"]
# print(x)

thisdict = {
    "brand": "ford",
    "model": "mustang",
    "year": 1964
}
x = thisdict.get("model")
print(x)




# car = {
#     "brand": "ford",
#     "model": "mustang",
#     "year": 1964
# }
# x = car.keys()
# print(x)

# car["color"] = "white"
# print(x)

# thisdict = {
#     "brand": "ford",
#     "model": "mustang",
#     "year": 1964
# }
# x = thisdict.values()
# print(x)




# car = {
#     "brand": "ford",
#     "model": "mustang",
#     "year": 1964
# }
# x = car.values()
# print(x)

# car["color"] = "red"
# print(x)

# thisdict = {
#     "brand": "ford",
#     "model": "mustang",
#     "year": 1964
# }
# x = thisdict.items()
# print(x)

# thisdict = {
#     "brand": "ford",
#     "model": "mustang",
#     "year": 1964
# }
# if "model" in thisdict:
#    print("yes, 'model' is one the keys in the thisdict dictionary")




# thisdict = {
#     "brand": "ford",
#     "model": "mustang",
#     "year": 1964
# }
# thisdict["color"] = "red"
# print(thisdict)

# thisdict = {
#     "brand": "ford",
#     "model": "mustang",
#     "year": 1964
# }
# thisdict.update({"color": "red"})
# print(thisdict)




# thisdict = {
#     "brand": "ford",
#     "model": "mustang",
#     "year": 1964
# }
# thisdict.pop("model")
# print(thisdict)

# thisdict = {
#     "brand": "ford",
#     "model": "mustang",
#     "year": 1964
# }
# thisdict.popitem()
# print(thisdict)




# thisdict = {
#     "brand": "ford",
#     "model": "mustang",
#     "year": 1964
# }
# del thisdict["model"]
# print(thisdict)

# thisdict = {
#     "brand": "ford",
#     "model": "mustang",
#     "year": 1964
# }
# del thisdict
# print(thisdict)




# thisdict = {
#     "brand": "ford",
#     "model": "mustang",
#     "year": 1964
# }
# thisdict.clear()
# print(thisdict)

# thisdict = {
#     "brand": "ford",
#     "model": "mustang",
#     "year": 1964
# }
# for x in thisdict.items():
#    print(x)




# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": "1964"
# }
# for x in thisdict:
#     print(thisdict[x])

# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": "1964"
# }
# for x in thisdict.values():
#     print(x)




# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": "1964"
# }
# for x in thisdict.keys():
#     print(x)

# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": "1964"
# }
# for x,y in thisdict.items():
#     print(x,y)




# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": "1964"
# }
# mydict = thisdict.copy()
# print(mydict)

# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": "1964"
# }
# mydict = dict(thisdict)
# print(mydict)




# myfamily = {
#     "child1": {
#       "name": "mimito",
#       "year": "2002"
#   },
#     "child2": {
#       "name": "Mirfayz",
#       "year": "2005"
#   },
#     "child3": {
#       "name": "Mirxon",
#       "year": "2014"
#   }
# }
# print(myfamily)
# new=myfamily["child1"]
# print(new["name"])





# child1 = {
#       "name": "mimito",
#       "year": 2002
#   }
# child2 = {
#       "name": "Mirfayz",
#       "year": 2005
#   }
# child3 = {
#       "name": "Mirxon",
#       "year": 2014
#   }

# myfamily = {
#     "child1": child1,
#     "child2": child2,
#     "child3": child3,
# }



# print(myfamily)
# print(myfamily["child1"]["name"])
    

