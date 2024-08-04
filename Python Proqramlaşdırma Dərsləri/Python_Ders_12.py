"""Struktur
for variable_name in sequence:                (sequence -> strings, lists, range)
    block
"""

# range()
for i in range(2, 5):
    print(i)

for computer in range(2, 7):
    if computer % 2 == 0:
        print(computer)
    else:
        print(computer - 2)

for i in range(2, 20, 3):
    if i > 10:
        print(i + 1)
    elif i < 7:
        print(i - 1)
    else:
        print(i * 2)

# String 
s = input() # Baku is a nice city!!!
say = 0
for i in s:
    if i == " ":
        say = say + 1
print(say)

# Lists
lst = [10, -4, 2, True, False, 5.6, "Bahruz", "Zaman"]
for i in lst:
    print(i)

lst = [5, 10, 2, -6]
for i in lst:
    if i % 2 == 0:
        print(i)
    else:
        print(i * 2)


# Examples
s = input("Sozu daxil edin: ") 
for i in range(len(s)):
    print(i, "-->", s[i])

# 20 -56 7823 0 -485 85 29
s = input().split() # ["20", "-56", "7823", "0", "-485", "85", "29"]
print("Evvelki siyahi:", s)
for i in range(len(s)):
    s[i] = int(s[i])
print("Sonraki siyahi:", s)
print(max(s))
