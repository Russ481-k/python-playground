result_1 = [33, 40, 12, 63, 52]
# 1-1
result_1.append(9)

# 1-2
result_1[1]=50

# 1-3
result_1[2:6]

# 1-4
result_1.sort(reverse=True)

#2-1
result_2=[]
total=0
for i in range(1,8):
    result_2.append(input(i,"일차 수입내역 : "))
    inputCount=int(result_2[i-1])
    print(total,inputCount)
    total += inputCount
avg=total/7
print(int(avg))
