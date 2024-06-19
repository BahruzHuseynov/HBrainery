# Şərtlər Qrupu - Yalnız 1 şərt bloku icra oluna bilər
# 1
"""
if şərt1:       # True or False
    icra1       # Block (Gövdə)
"""
# Indentation (Indentasiya)
x = 5
if x % 2 == 1 and x > 2 and 5 in [2,3,4,5]:
    x = x - 1 # 4
    print(x * 2) # 8
    print(x * 3) # 12

# 2
"""
if şərt1:
    icra1
else:
    icra2
"""
x = 4
if x % 2 == 1:
    print(x * 2)
else:
    print(x * 3)


# 3
"""
if şərt1:
    icra1
elif şərt2:
    icra2
"""
x = 10
if x > 5:
    print(x + 5)
elif x > 8:
    print(x + 8)

if x > 5:
    print(x + 5)
if x > 8:
    print(x + 8)

# 4
"""
if şərt1:
    icra1
elif şərt2:
    icra2
else:
    icra3
"""
x = 3
if x > 8:
    print(x * 2)
elif x > 5:
    print(x * 3)
else:
    print(x * 4)

# 5
"""
if şərt1:
    icra1
elif şərt2:
    icra2
elif şərt3:
    icra3
else:
    icra4
"""
qiymet = 45
if qiymet > 90:
    print("A")
elif qiymet > 80:
    print("B")
elif qiymet > 70:
    print("C")
elif qiymet > 60:
    print("D")
elif qiymet > 50:
    print("E")

# 6
"""
if şərt1:
    icra1
elif şərt2:
    icra2
elif şərt3:
    icra3
"""

# Fərqli kodlar
# 1
x = input()
if "4" in x:
    print("Bəli, ədəddə 4 rəqəmi var")
else:
    print("Xeyr, ədəddə 4 rəqəmi yoxdur")

x = 100
a = "Baku"
if x > 50:
    print(x * 2) # 200
    if x > 120:
        print(x * 3) 
        if a.lower() == "baku":
            print(a * 2) 
