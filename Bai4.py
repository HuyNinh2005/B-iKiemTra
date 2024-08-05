n = input().split()
s = []
for i in n:
    for char in i:
        s.append(char)
s1 = set(s)
print(list(s1))