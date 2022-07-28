num1, num2 = map(int, input("두 정수를 입력해주세요").split())

alldata = [num1 * i for i in range(1, num2 + 1)]


for i in alldata:
    if i % num2 == 0:
        print(f"{num1}, {num2}의 최소공배수는 {i} 입니다.")
        break