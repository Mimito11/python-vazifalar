# 1-topwiriq

# thisdict = {
#     "Otamning ismi":"Jahongir",
#     "Tugilgan yili":"1974-yilda",
#     "Manzil":"Gijduvon tuman",    
# }
# print(thisdict)




# 2-topwiriq

# thisdict = {
#     "choson": "Mirxonning sevimli taomi Shashlik",
#     "amir": "Amirbekning sevimli taomi Kobob",
#     "mirka": "Meronning sevimli taomi Osh",
#     "jaxa": "Javohirning sevimli taomi Baliq",
#     "mimito": "Mening sevimli taomim Somsa",
# }
# print(thisdict["choson"])
# print(thisdict["amir"])
# print(thisdict["jaxa"])




# 3-topwiriq

# thisdict = {
#     "integer":"butun son",
#     "float":"suzmoq",
#     "string":"ip",
#     "if":"agar",
#     "else":"boshqa", 
#     "upper":"yuqori",
#     "lower":"pastroq",
#     "strip":"tasma",
#     "replace":"almashtir",
#     "input":"kiritish",
#     "append":"qo'shish"
# }
# print(thisdict)




#4-topshiriq

thisdict = {
    "integer":"butun son",
    "float":"suzmoq",
    "string":"ip",
    "if":"agar",
    "else":"boshqa", 
    "upper":"yuqori",
    "lower":"pastroq",
    "strip":"tasma",
    "replace":"almashtir",
    "input":"kiritish",
    "append":"qo'shish"
}

kiritish = input("So'z kirit: ")

x = thisdict.get(kiritish)
if x:
    print(x)
else:
 print("Bunday so'z mavjud emas!")






