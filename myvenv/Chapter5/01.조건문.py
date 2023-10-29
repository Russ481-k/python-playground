origin_password="1234"
input_password=input("비밀번호를 입력하세요>>>")

if origin_password==input_password:
    print("비밀번호가 일치합니다.")
elif input_password=="": 
    print("비밀번호를 입력해주세요.")
else:
    print("비밀번호가 일치하지 않습니다.")