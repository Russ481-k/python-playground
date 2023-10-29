#사용자로부터 생일 연도를 입력 받고 나이 출력하기
from datetime import datetime

birthYear=int(input("태어난 연도를 입력하세요>>>"))

now = datetime.now().year
print(now-birthYear)