count = 1

while count < 11:
    print(f"{count}바퀴째")
    count += 1
    
print("달리기를 마쳤습니다.")

# 이걸 break로 바꿔보자

count = 1

while True:
    print(f"{count}바퀴째")
    count += 1
    if count >= 10:
        # 10이 되는 순간 참이 저 조건이 참이 되어 루프가 종료함
        break

print("달리기를 마쳤습니다.")
# break는 반복문을 중단시키는 역할을 함


#이때, 19바퀴째에 멈추고 싶다면?
count = 0

while True:
    count += 1
    if count == 19:
        print("쉬어야겠다...")
        continue

    print(f"{count}바퀴째")
    if count == 20:
        break

print("달리기를 마쳤습니다.")
# 19바퀴 때 쉬어야겠다... 출력되고, 20바퀴 때는 달리기를 마쳤습니다. 출력됨
# continue는 특정 조건에서 그 회차를 쉬고, 다음 회차로 넘어가게 하는 역할을 함
#다시 설명하자면,

for i in range(20):
    print(i)
# 0-20까지 출력됨

for i in range(20):
    if i ==5:
        break
# 0-4까지 출력됨, 5에서 멈춤
    print(i)
    
    
for i in range(20):
    if i == 5:
        continue

    print(i)
# 0-4, 6-19까지 출력됨, 5는 출력되지 않음