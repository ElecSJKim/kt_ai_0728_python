num = int(input("정수를 입력하세요: "))

temp = 0

for root in range(2, num):
    for pwr in range(2, 6):
        if root ** pwr == num:
            temp = 1
            print(f"{root}**{pwr}")

if not(temp):
    print("결과가 없음")