
def f(number):
    maximum = number[0]
    for i in range(1, len(number)):
        if number[i] > maximum:
            maximum = number[i]

    return maximum

number = []
for _ in range(4):
    number.append(int(input("정수를 입력해주세요")))

print(f"최대값은 {f(number)} 입니다.")