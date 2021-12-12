# biror elementni quwiw ucun
aLsit = [100, 200, 300, 400, 500]
aLsit = aLsit[::-1]
print(aLsit)


list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)


list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "i"], "m", "n"]
list2 = ["h", "i", "j"]
list1[2][1][2].append(list2)
print(list1)
