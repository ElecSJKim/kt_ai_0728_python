def electricPay(use):
    if use < 100:
        total = 410 + use * 60.7
    elif use <= 200:
        total = 910 + 60.7*100 + 125.9*(use-100)
    else:
        total = 1600 + (60.7 + 125.9)*100 + 187.9*(use-200)

    return total * 1.137

elec = int(input("전기 사용량을 입력해주세요"))
print(f"최종 전기 요금은 : {int(electricPay(elec))}원 입니다.")