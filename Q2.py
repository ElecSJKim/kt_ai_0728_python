def cycle(number):
    if int(number) < 10:
        number ='0' + number

    backnum = int(number[0]) + int(number[-1])
    backnum %= 10

    return number[-1] + str(backnum)

num = input("정수를 입력해주세요")
a = num
count = 0

while True:
    a = cycle(a)
    count += 1

    if int(a) == int(num):
        print(count)
        break