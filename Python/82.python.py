# x,y=5,10
# try:
#     y/(x-5)
# except ZeroDivisionError:
#     print("0 ga bo'lib bo'lmaydi")


    

# mevalar = ['olma', 'anor', 'anjir', 'uzum']
# try:
#     print(mevalar[7])
# except IndexError:
#     print(f"Ro'yxatda {len(mevalar)} ta meva bor xolos")




# user = {"username":"sariqdev",
#         "status":"admin",
#         "emile":"admin@sariq.dev",
#         "phone":"998914019393",
#         "tel":"902988080"}
# key = "tel"
# try:
#     print(f'foydalanuvchi: {user["tel"]}')
# except KeyError:
#     print("Bunday kalit mavjud emas")




n = input("butun son kiriting: ")
try:
    n = int(n)
    x = 20/n
except ValueError: #agar foydalanuvchi butun son kiritmasa
    print("Butun son kiritmadingiz")
except ZeroDivisionError: #agar foydalanuvchi 0 kiritsa
    print("0 ga bo'lib bo'lmaydi")
else:
    print(f"x = {x}")
