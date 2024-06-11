# Sual 1
import math
x = int(input())
print(x**3 - x**2)
print(math.pow(x, 3) - math.pow(x, 2))

# Sual 2
s = input() # s = "364"
for i in s: 
    print(f"{int(s) / int(i):.2f}", end = " ")

# Sual 3
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
p = (a+b+c)/2
S = (p*(p-a)*(p-b)*(p-c))**0.5
print(S)

# Sual 4
s = int(input()) # 2002
komek = s
ikinci = 0
while s > 0:
    q = s % 10
    ikinci = ikinci * 10 + q 
    s = s // 10 
print(ikinci == komek)

# Sual 5
s = input() # s = "1012"
x = ""
for i in s:
    if i != "1":
        x += i
print(int(x))