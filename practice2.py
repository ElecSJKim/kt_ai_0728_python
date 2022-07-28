print("+ 와 -를 번갈아 출력합니다.")
num = int(input("몇 개를 출력할까요? "))

for _ in range(num//2):
    print("+-",end="")

if num % 2 == 1:
    print("+")
else:
    print()