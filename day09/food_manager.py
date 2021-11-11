

import sys

# 메뉴데이터를 저장할 딕셔너리
# 저장 예시: {'짜장면': 4000, '짬뽕': 3000}
foods = {}

while True:

    print("\n\n====== 음식점 메뉴 관리 프로그램 ======")
    print("# 1. 신규 메뉴 등록하기")
    print("# 2. 메뉴판 전체보기")
    print("# 3. 프로그램 종료하기")
    print("=========================================")
    select = input("# 메뉴 입력: ")
    if select == '1':        
        food = input('메뉴명: ')
        price = input('가격: ')
        foods[food] = price
    elif select == '2':
        print('\n======메뉴판======')
        for menu in foods:
            print(f' {menu} : {foods[menu]}원')
            print('==================')
            print('1. 수정 | 2. 삭제 | 3. 나가기')
            choice = input('=> ')
        if choice == '1':
            print('가격을 변경할 메뉴의 이름을 입력하세요.')
            old_food = input('=> ')
            if old_food in foods:
                change_pirce = input('변경할 가격: ')
                foods[food] = change_pirce
                print(f'{old_food}의 가격이 {change_pirce}원으로 변경되었습니다.')
            else:   
                print(f'{old_food}는(은) 등록된 메뉴가 아닙니다.')
        elif choice == '2':
            print('삭제할 메뉴명을 입력하세요.')
            del_food = input('=> ')
            del(foods[del_food])
                
        elif choice == '3':
            continue
    elif select == "3":
        print("# 프로그램을 종료하시겠습니까?[Y/N]")
        choice = input("=> ")
        if choice.lower()[0] == "y":
            print("프로그램을 종료합니다.")
            sys.exit()
        else:
            print("종료를 취소합니다.")
            continue
    else:
        print("메뉴를 잘못 입력했습니다.")

    input("\n메뉴를 보시려면 Enter....") 
