# no.2
import random
# no.1
print('~~~~~~~~~ 재미있는 사칙연산 게임 ~~~~~~~~')
print('[즐겁게 문제를 푸시다가 지겨우면 0을 누르세요~')
print('===========================================')

print('~~~~~~~ # 난이도를 설정합니다.~~~~~~~.')
print(' [ 1. 상 (1~100) | 2. 중 (1~50) | 3. 하 (1~20) ]')
level = int(input('>>> '))
if level == 1:
    levelNum = 100
elif level == 2:
    levelNum = 50
elif level == 3: 
    levelNum = 20
else:
    levelNum = 999
    print('난이도 선택이 잘못되었으므로 지옥난이도로 자동시작합니다.')


qNum = 1
ok = 0 #정답 횟수
no = 0 # 틀린 횟수
while True:
    # no.3
    first = random.randint(1, levelNum)
    second = random.randint(1, levelNum)


    #no 7 연산기호를 결정할 랜덤 숫자 생성 version3
    markNum = random.randint(1,3)

    if markNum == 1:
        mark = '+'
        real = first + second
    elif markNum == 2:
        # 같은 수 - 나왔을떄 0 입력하면 게임이 종료되는 버그를 고치기위해서 조작
        # if first == second
        # second -=1
        mark = '-'
        real = first - second
    else:
        mark = 'x'
        real = first * second

    #no. 5
    print(f'\nQ{qNum}.{first} {mark} {second} = ??')
    qNum += 1
    # 실제 정답
    

    # no.4 사용자의 입력각
    answer = int(input('>> '))

    # 종료 조건  version2 추가
    if answer == 0:
        # 같은수 뺴기 했을때 0이 나오면 종료가 되니까 조건을 0이아닌 그만 으로 바꿀수있음
        print('게임을 종료합니다!')
        print('------------------------------')
        print(f'정답횟수: {ok}회, 틀린횟수: {no}회') # 버전2
        break
    
    if real == answer:
        print('정답입니다!!')
        ok += 1 #버전 2 추가
    else:
        print('틀렸어요~~')
        no += 1 #버전 2 추가