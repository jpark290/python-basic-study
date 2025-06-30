#모듈은 어떠한 기능의 파이선 코드를 담고 있는 파일
#모듈은 정말많아서, 일단 몇가지만 배워보자.

#모듈을 불러오는 방법
import time
print(1)
time.sleep(2)
print(2)
# time 모듈을 사용하여 프로그램을 2초 동안 일시 중지합니다.

import time
for i in range(1, 11):
    print(f"{i} : hi!")
    time.sleep(1)
    
# random 모듈을 사용하여 무작위 숫자를 생성합니다.

import random
x = random.random()
print(x)  # Prints a random float between 0.0 and 1.0

x = random.randint(1, 10)
print(x)  # Prints a random integer between 1 and 10 (inclusive)

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(x)
print(x)  # Shuffles the list in place, randomizing the order of elements

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = random.choice(x)
print(y)  # Randomly selects an element from the list x


x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = random.sample(x, 3)
print(y)  # Randomly selects 3 unique elements from the list x

# 날짜와 시간 관련 모듈도 있음
import datetime
today = datetime.date.today()
print(today)  # Prints today's date in the format YYYY-MM-DD
print(today.month)  # Prints the current month (1-12)


#os 모듈
import os
print(os.getcwd())  # Prints the current working directory
print(os.listdir())  # Lists all files and directories in the current directory