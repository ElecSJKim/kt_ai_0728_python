num = int(input("직사각형의 넓이를 입력하세요.:"))

for i in range(1, num+1):
    for j in range(1, num+1):
        if i*j > num:
            continue
        
        if i*j == num:
            print(f'{i} x {j}')