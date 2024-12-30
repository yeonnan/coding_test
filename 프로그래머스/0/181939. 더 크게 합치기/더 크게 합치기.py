def solution(a, b):
    num1 = int(str(a) + str(b))
    num2 = int(str(b) + str(a))
    
    if num1 > num2:
        return num1
    else:
        return num2