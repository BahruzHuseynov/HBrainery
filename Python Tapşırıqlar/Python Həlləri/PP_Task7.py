# Sual 1
x = int(input())
if x % 2 == 0:
    print(x + 1)
else:
    print(x + 2)

# Sual 2
x = input().split() # ["-3","2","5","10","5","-5","0"]
say = 0
for i in range(len(x)): 
    if i == 0:
        if int(x[i + 1]) % 2 == 0:
            say += 1
    elif i == len(x) - 1:
        if int(x[i - 1]) % 2 == 0:
            say += 1
    else:
        if int(x[i - 1]) % 2 == 0 and int(x[i + 1]) % 2 == 0:
            say += 1
print(say)

# Sual 3
x = input()
ters = x[::-1]
print(int(x) - int(ters))

# Sual 4
x = input() # '573'
lst = ["55", "33", "35", "53"]
logic = False
for i in range(len(x) - 1):
    if x[i:i+2] in lst:
        logic = True
print(logic)

# Sual 5
print(len(input().split()))