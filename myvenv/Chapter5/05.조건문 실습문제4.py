koreanScore=int(input("국어 시험 점수를 입력하세요>>>"))
mathScore=int(input("수학 시험 점수를 입력하세요>>>"))
englishScore=int(input("영어 시험 점수를 입력하세요>>>"))

totalScore=koreanScore+mathScore+englishScore
avgScore=totalScore/3

if 0>koreanScore>100 or 0>mathScore>100  or 0>englishScore>100 :
    print("시험 점수를 잘못 입력하였습니다.")
else:
    if avgScore>=80:
        print("불합격입니다.")
    else:
        print("합격입니다.")

    
    
