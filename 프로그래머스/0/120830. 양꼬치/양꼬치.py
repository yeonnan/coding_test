def solution(n, k):
    s = n//10
    answer = n*12000 + (k-s)*2000
    return answer