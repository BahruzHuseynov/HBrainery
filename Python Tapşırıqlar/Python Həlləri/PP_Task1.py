# Sual 1
x = input() # 931912
ilk = x[:3] # 931
ikinci = x[3:] # 912
say1 = ilk.count("1") # 1
say2 = ikinci.count("1") # 1
if say1 == say2 and "1" in x:
    print(True)
else:
    print(False)

# Sual 2
x = input().split()
for i in x:
    print(i[::-1], end = " ")

# Sual 3
x = abs(int(input()))
s = 0
while x > 0:
    q = x % 10 
    s = s + q 
    x = x // 10 
print(s)

# Sual 4
x = input().split() # ["2","5","6","7","4"]
x.remove(max(x)) # ["2","5","6","4"]
x.remove(max(x)) # ["2","5","4"]
x.sort() # ["2","5","4"]
if x[0] == "0":
    x[0], x[1] = x[1], x[0]
print("".join(x))

# Sual 5
x = input().split() 
for i in x:
    if int(i) % 2 == 0:
        print(int(i) + 2, end = " ")
    else:
        print(int(i) + 1, end = " ")