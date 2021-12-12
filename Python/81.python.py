# import datetime
# x = datetime.datetime.now()
# print(x)

# x = datetime.datetime.now()
# print(x.year)
# print(x.strftime("%d"))
# print(x.strftime("%A"))
# print(x.strftime("%B"))




# x = min(5, 10, 25)
# y = max(5, 10, 25)
# print(x)
# print(y)

# x = abs(-7.25)
# print(x)

# x = pow(4, 3)
# print(x)




# import math
# x = math.sqrt(64)
# print(x)

# import math
# x = math.ceil(1.4)
# y = math.floor(1.4)
# print(x)
# print(y)

# import math
# x = math.pi
# print(x)




# import json
# x = '{"name":"mimito", "age":16, "city":"New York"}'
# y = json.loads(x)
# print(y["age"])




# import json
# x = {
#     "name": "mimito",
#     "age": 16,
#     "city": "gij"
# }
# y = json.dumps(x)
# print(y)




# import json
# x = {
#     "name": "mimito",
#     "age": 30,
#     "married": True,
#     "divorced": False,
#     "children": ("Ann","Billy"),
#     "pets": None,
#     "cars": [
#         {"model": "BMW 230", "mpg": 27.5},
#         {"model": "Ford Edge", "mpg": 24.1}
#     ]
# }
# y = json.dumps(x)
# print(y)




# try:
#     print(x)
# except:
#    print("x ga biror narsa yoz!")



# x = 5
# try:
#     print(x)
# except NameError:
#    print("x ga narsa yoz!")
# except:
#    print("x ga yoz!")




# try:
#     print("Hello")
# except NameError:
#    print("x ga narsa yoz!")
# else:
#    print("x ga yoz!")




# try:
#     print("Hello")
# except NameError:
#    print("x ga narsa yoz!")
# finally:
#    print("x ga yoz!")




# try:
#     f = open("demofile.txt")
#     try:
#         f.write("lorem ipsum")
#     except:
#         print("x ga narsa yoz!")
#     finally:
#         f.close()
# except:
#     print("x ga yoz!")




x = 1
if x < 0:
    raise Exception("Sorry, no numbers below zero")

x = "Hello"
if not type(x) is int:
  raise TypeError("Only integers are allowed")

