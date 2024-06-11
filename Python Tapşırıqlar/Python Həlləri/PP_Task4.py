# Sual 1
x = input() # "Baku"
u = len(x) # 4
print(u, u % 2 == 0)

# Sual 2
x = input()
p = 1
for i in x: 
    p = p * int(i) 
print(p)

# Sual 3
a, b, k = input().split() # 4 7 5
a = float(a)
b = float(b)
k = float(k)
print(a * b == k**2)

# Sual 4
x = abs(int(input()))

def uzunluq(x): 
    say = 0
    while x > 0:
        say += 1 
        x //= 10 
    return say

say = uzunluq(x)
a = x // 10 ** (say-1)
b = x % 10
if a == b:
    print("=")
else:
    print(max(a, b))

# Sual 5
a, b = input().split() # 7 5
a = int(a) # 7
b = int(b) # 5
if a > b:
    a, b = b, a

s = 0
if a != b:
    for i in range(a, b + 1):
        s += i
print(s)