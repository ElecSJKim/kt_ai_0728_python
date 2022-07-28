from math import sqrt

def solution(n):
    num = sqrt(n)

    if num % 1.0 == 0:
        return int((num+1) ** 2)
    else:
        return -1

n = int(input("정수를 입력해주세요"))

print(solution(n))