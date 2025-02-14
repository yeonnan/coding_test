n = int(input())
a = []

for i in range(n):
    a.append(int(input()))
b = sorted(a)

for i in range(len(a)):
    print(b[i])