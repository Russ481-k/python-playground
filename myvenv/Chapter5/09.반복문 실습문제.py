# 1 
multiplicationTableNumber = int(input("구구단 몇 단을 계산할까요? : "))

for i in range(1,10):
    print(multiplicationTableNumber,"*",i,"=",multiplicationTableNumber*i)

# 2
programNumber=int(input("프로그램을 시작하려면 1을 입력하세요>>>"))
while True:
    print("[메뉴를 입력하세요]")        
    programNumber=int(input("1. 프로그램 시작 2. 실시간 랭킹 3. 프로그램 종료 >>>"))
    if programNumber == 1:
        print("->프로그램 실행중")
    elif programNumber == 2:
        print("->실시간 랭킹")
    elif programNumber == 3:
        print("->프로그램을 종료합니다.")
        break
    else:
        print("->1~3의 숫자를 입력하세요.")


# 3
words=["사과", "바나나", "파인애플", "포도", "오렌지"]
for word in words:
    print(word)
    typingWord=input("위에 있는 단어를 그대로 입력하세요>>>")
    if typingWord == word:
        print("정답입니다.")
    else:
        print("오답입니다.")
        break
print("종료합니다.")
# 4