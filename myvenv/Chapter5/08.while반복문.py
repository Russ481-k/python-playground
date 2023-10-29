count = 0
while count < 10 :
    print(count,"번째 반복")
    count = count + 1

while True :
    print("반복을 계속할까요?(예/아니오)")
    answer = input()
    if answer == "아니오" :
        break
    print("반복을 계속합니다.")
