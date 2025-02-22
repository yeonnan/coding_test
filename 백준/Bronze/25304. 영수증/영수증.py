X = int(input())
N = int(input())
result = 0

for i in range(0, N):
    A, B = map(int, input().split())
    result += A*B

if result == X:
    print('Yes')
else:
    print('No')