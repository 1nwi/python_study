
# 랜덤 로또번호 만들기
import random

# 당첨번호
win_lotto = []
my_lotto = []

while len(win_lotto) < 6:
    rn = random.randint(1,45) # 1~45 난수 생성
    if rn not in win_lotto:
        win_lotto.append(rn)

# win_lotto.sort()
# print('당첨 번호:', win_lotto)

#  보너스 번호 생성
while True:
    bonus_x = random.randint(1, 45)
    if bonus_x not in win_lotto:
        bonus = bonus_x
        break
# print(f'보너스 번호: {bonus}')

#---------- 반복을 실행해야 하는 구간 -----------

paper = 0
while True:

    # 내가 구매한 번호
    my_lotto = []

    while len(my_lotto) < 6:
        rn = random.randint(1,45) # 1~45 난수 생성
        if rn not in my_lotto:
            my_lotto.append(rn)

    # my_lotto.sort()
    paper += 1
    # print('내 번호:', my_lotto)

    # =========================================================

    count = 0   # 맞춘 개수를 저장

    '''  
    *복잡한 방법*
    for n in my_lotto:
        for m in win_lotto:
            if n == m:
                count += 1
                break
    '''

    for n in my_lotto:
        if n in win_lotto:
            count += 1

    if count == 6:
        print('1등에 당첨되었습니다!')
        break
    else:
        print(f'로또 {paper}장쨰 구매중.....')


    # print(f'맞춘 개수: {count}개')

'''
*잠시 주석처리*
# 등수 체크
if count == 6:
    print('1등!')
elif count == 5:
    if bonus in my_lotto:
        print('2등!')
    else:
        print('3등!')
elif count == 4:
    print('4등!')
elif count == 3:
    print('5등!')
else:
    print('꽝!')
'''