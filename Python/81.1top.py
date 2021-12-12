yosh = input("Yoshingizni kiriting: ")
yosh = int(yosh)
print(f"Siz {2021-yosh} yilda tugilgansiz")

yosh = input("Yoshingizni kiriting: ")
try:
    yosh = int(yosh)
    print(f"Siz {2021-yosh} yilda tugilgansiz")
except:
    print("Butun son kiritmadingiz")
print("Dastur tugadi!")