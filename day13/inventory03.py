# 전역변수 정의부
inventory = []
import sys
# 함수 정의부

# 제품 번호의 중복을 확인하는 함수
def check_duplicate_code():
    while True:
        code = input('- 제품 번호: ')
        flag = False # 중복 플래그
        # 중복 검증 
        for p in inventory:
            if code == p['제품번호']:
                # 중복됨
                print('# 제품 번호가 중복되었습니다. 다시 입력하세요!')
                flag = True
                break
        if flag ==False:
            return code

# 제품등록을 수행하는 함수
def insert_product():
    product = {}
    print('\n# 제품 정보 등록을 시작합니다.')    

    product['제품번호'] = check_duplicate_code()
    product['제품명'] = input('- 제품명: ')
    product['가격'] = int(input('- 가격: '))
    product['수량'] = int(input('- 수량: '))
    product['총액'] = product['가격'] * product['수량']

    inventory.append(product)
    # print('\n# 제품 등록이 정상처리되었습니다.')
    


# 메인 실행부
if __name__ == '__main__':
    
    while True:
        print('\n*** 재고 관리 프로그램 ***')
        print('# 1. 제품 정보 등록하기')
        print('# 2. 모든 제품정보 조회')
        print('# 3. 개별 제품정보 조회')
        print('# 4. 제품정보 수정하기')
        print('# 5. 제품정보 삭제하기')
        print('# 6. 프로그램 종료하기')
        menu = int(input('# 메뉴입력: '))

        if menu == 1:
            insert_product()
        elif menu  ==2:
            print(' *** 창고 재고 정보 ***')
            print(inventory)
        elif menu == 6:
            print("# 프로그램을 종료하시겠습니까?[Y/N]")
            choice = input("=> ")
            if choice.lower()[0] == "y":
                print("프로그램을 종료합니다.")
                sys.exit()
            else:
                print("종료를 취소합니다.")
                continue
        
        