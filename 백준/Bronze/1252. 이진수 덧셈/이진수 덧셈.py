a, b = map(str, input().split())
a = int(a, 2)
b = int(b, 2)
c = a+b

print(bin(c)[2:])        # bin : 10진수를 2진수로 변환