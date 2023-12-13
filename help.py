expct = 20
Pp = 100

num13 = int(input("Enter num13 : "))
denum13 = int(input("Enter denum13 : "))

Ex = expct / 100

pr = num13 / denum13
pr1 = pr * Pp

exNum = pr1 * Ex


exDenum = (denum13 / denum13) * expct

over = ((0 + exNum) / (0 + exDenum)) * 100

print(over)