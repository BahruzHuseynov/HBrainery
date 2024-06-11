# Sual 1
def ugurlu(x):
    for i in str(x):
        if i not in "257":
            return False
    return True

n = int(input())
i = 0
while n > 0:
    i = i + 1
    if ugurlu(i):
        n = n - 1 # n-=1
print(i)

# Sual 2
x = input()  
if x[0] == "-":
    x = x[1:]
logic = True
for i in x:
    if i not in "0123456789":
        logic = False
print(logic and x[0] != "0")

# Sual 3
x = abs(int(input()))
c = 0
while x > 0:
    q = x % 10
    if q % 2 == 0:
        c = c + 1
    x = x // 10
print(c)

# Sual 4
S, h = input().split()
S = float(S)
h = float(h)
AB = 2*S/h
print(AB)

# Sual 5
print(len(input()))