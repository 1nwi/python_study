

import random

# 게임의 정답: 1 ~ 20사이의 랜덤 정수


print('~~~~~~~재미있는 사칙연산 게임~~~~~~~')
print('[즐겁게 문제를 푸시다가 지겨우면 0을 누르세요~]')
print('=' * 30)

print('~~~~~~~난이도를 설정합니다.~~~~~~~.')
print(' [ 1. 상 (1~100) | 2. 중 (1~50) | 3. 하 (1~20) ]')
level = int(input('>>> '))
if level == 1:
    
    count_down = 4
elif level == 2:
    
    count_down = 6
elif level == 3:
    
    count_down = 8
else:
    print('난이도 선택이 잘못되었으므로 상난이도로 자동시작합니다.')
    

count = 0
win = 0
lose =0
while True:

    secret = random.randint(1, 20) 
    secret_two = random.randint(1, 20)
    count += 1
    
    operation = random.randint(1, 3)
    if operation == 1:
        print(f'\nQ{count}. {secret} + {secret_two} = ?? ')
        number = int(input('>> '))
    elif operation == 2:
        print(f'\nQ{count}. {secret} - {secret_two} = ?? ')
        number = int(input('>> '))
    else:
        print(f'\nQ{count}. {secret} x {secret_two} = ?? ')
        number = int(input('>> '))

    question_one = secret + secret_two
    question_two = secret - secret_two
    question_three = secret * secret_two

    
    if number == 0:
        print('게임을 종료합니다!')
        print('=====' * 10)
        print(f'정답횟수: {win}회, 틀린횟수: {lose}회')
        break
    elif number == question_one or question_two or question_three:
        print('정답입니다!')
        win += 1
    else:
        print('틀렸어요~')
        lose += 1