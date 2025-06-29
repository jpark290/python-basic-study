#for로 구구단 출력하기

for i in range(2, 10):
    print(i)
#범위가 맞는지 확인해보자 - 맞음

for i in range(2, 10):
    print(f"<< {i}단 >>")
    for j in range(1, 10):
        result = i * j
        print(f"{i} * {j} = {result}")
        #반복문 안에 반복문 가능함 - 그러니, i가 2일때 j가 1부터 9까지 반복하고, i가 3일때 j가 1부터 9까지 반복하는 식임
    
print("구구단을 완료했습니다.")
        