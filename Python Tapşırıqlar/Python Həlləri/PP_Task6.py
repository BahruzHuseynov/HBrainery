# Sual 1
x = input()
print(x.replace(" ", ""))

# Sual 2
x = int(input())
def factorial(x):
    if x <= 1:
        return 1
    return x * factorial(x-1)
print(factorial(x))

# Sual 3 (ASCII)
x = list(input().lower()) 
x.sort() 
print("".join(x))

# Sual 4
x = input().split()
mx = int(x[0]) 
for i in x:
    if mx < int(i):
        mx = int(i)
print(mx)

# Sual 5
x = int(input())
kok_alti = x ** 0.5
if kok_alti == int(kok_alti):
    print("Beli", int(kok_alti))
else:
    print("Xeyr")








