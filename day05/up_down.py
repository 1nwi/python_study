#up donw 게임 
'''
1. 랜덤 정답이 필요함. 1 ~ 100 사이 정수를 생성해야함.
2. 사용자가 정답을 입력할 수 있게 해야함.
3. 비교후 UP인지 DONW인지ㅣ 판단해줌
4. 정답을 맞출 때까지 지속적으로 사용자가 정답을 입력할 수 있어야 한다.

-> 입력하는 코드 + 검사하는코드 반복해야할 필요가 있다.
-> 근데 반복횟수를 사전에 알기가 어려움.
-> 무한루프를 써야 하겠다.

5. 사용자에게 입력값의 범위를 힌트로 알려주고싶음 그래서 최소값을 저장할 min
    최대값 max를 각각 만듬

    현재 정답이 37이라고 가정 그런데 사용자가 50을 입력함
    ->DOWN상황 -> 다음번 범위는 1 ~ 50 -> max가 사용자의 입력값으로 변경
    현재 정답이 37이라고 가정 그런데 사용자가 14를 입력함
    ->UP상황 -> 다음번 번위는 14 ~ 50 -> min이 사용자의 입력값으로 변경
 
 6. 정답을 몇번만에 맞췄는지 알려주기
    -> 입력 기회가 몇번이었는지 카운팅하면 될것같음
    -> 카운트를 저장할 변수가 필요함.
 '''


import random

# 게임의 정답: 1 ~ 100사이의 랜덤 정수
secret = random.randint(1, 100) 


print('[UP & Down 게임 - 1~100 사이의 숫자중 어떤 숫자가 들어있을까요???]')
print('-' * 40)

min = 1
max = 100
count = 0
count_down = 6

# 난이도 설정
print('# 게임의 난이도를 선택하세요.')
print(' [ 1. 상 | 2. 중 | 3. 하 ]')
level = int(input('>>> '))
if level == 1:
    print('난이도 상을 선택했습니다. 기회가 4번 주어집니다.')
    count_down = 4
elif level == 2:
    print('난이도 중을 선택했습니다. 기회가 6번 주어집니다.')
    count_down = 6
elif level == 3:
    print('난이도 하을 선택했습니다. 기회가 8번 주어집니다.')
    count_down = 8
else:
    print('난이도 선택이 잘못되었으므로 상난이도로 자동시작합니다.')
    count_down = 4

while True:

    #카운트다운이 소진되었을 시점에 알림메시지 제공
    if count_down == 0:
        print('승리 기회가 날아갔습니다. 그러나 문제를 계속 풀어주세요!')

    # 사용자의 입력
    if count_down > 0:
        answer = int(input(f'\n# 숫자를 입력하세요({min} ~ {max} | {count_down}번 남았습니다.): '))
    else:
        answer = int(input(f'\n# 숫자를 입력하세요({min} ~ {max}): '))
        

    # 범위 안의 값을 입력했는지 검증
    if (min > answer) or (max < answer):
        print('\n# 범위를 벗어난 값을 입력했습니다.')
        continue
    
    # 입력카운트 증가
    count += 1
    count_down -= 1
    
    if secret == answer:
        print(f'정답입니다!! {count}번만에 맞추셨네요!')
        if count_down >= 0:
            print('YOU WIN!!')
        else:
            print('YOU LOSE!!')    
        break
    elif secret > answer:
        print('UP!!')
        min = answer
    else:
        print('DOWN!!')
        max = answer


