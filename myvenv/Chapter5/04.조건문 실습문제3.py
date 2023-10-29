totalBudget=int(input("예산을 입력하세요>>>"))
if totalBudget>=20000:
    print("오늘 저녁은 치킨.")
elif totalBudget>=10000:
    print("오늘 저녁은 떡볶이.")
elif totalBudget>=2000:
    print("오늘 저녁은 편의점 김밥.")
else:
    print("굶어야겠지.")