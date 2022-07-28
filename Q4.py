data = input('숫자로 이루어진 문자열을 입력하세요. ')

result = int(data[0])

for i in range(1, len(data)):
    if result > 1 and int(data[i]) > 1:
        result *= int(data[i])
    else:
        result += int(data[i])

print(result)