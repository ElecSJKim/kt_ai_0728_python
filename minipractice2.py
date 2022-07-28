def waterPay(company, use):

    if company == 'A':
        return use * 100
    elif company == "B":
        if use <= 50:
            return use * 150
        else:
            return 150*50 + (use-50)*75
        

company, use = input("수도회사와 수도 사용량을 입력하세요\n").split()

print(f"수도 회사는 {company}이며, 요금은 {waterPay(company, int(use))} 입니다.")