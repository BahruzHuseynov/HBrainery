# Sual 1
x = input() # "a2b"
logic = False
for i in x:
    if i in "0123456789":
        logic = True
print(logic)

# Sual 2
x = input() # Baku
print(x[::2])

# Sual 3
a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)
if a == 0:
    print("Kvadrat tenlik deyil")
else:
    D = b**2 - 4*a*c
    if D > 0:
        x1 = (-b + D**0.5)/(2*a)
        x2 = (-b - D**0.5)/(2*a)
        print(x1, x2)
    elif D == 0:
        x = -b/(2*a)
        print(x)
    else:
        print("Koku yoxdur")

# Sual 4
x = input() # Ahmad
c = len(x)
if c % 2 == 0:
    print(x[c//2-1])
else:
    print(x[c//2])

# Sual 5
x = input() 
s = 0
for i in x:
    s = s + int(i)
print(s)