n = input('숫자를 입력하세요. ')

length = len(n)//2
front = behind = 0

for i in range(length):
    front += int(n[i])
    behind += int(n[-i-1])

if front == behind:
    print("LUCKY")
else:
    print("READY")