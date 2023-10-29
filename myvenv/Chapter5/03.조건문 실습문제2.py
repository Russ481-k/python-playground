totalStudyTime=int(input("총 공부시간을 입력하세요>>>"))
if totalStudyTime>=10:
    print("휴대폰 잠금이 해제됩니다.")
elif totalStudyTime>=5:
    print("휴대폰을 30분간 사용가능 합니다.")
else:
    print("휴대폰 사용이 불가능합니다.")