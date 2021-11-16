#######################################################
# 함수 정의
def add(n1, n2):
    print(f'{n1}, {n2}')
    return n1 + n2
    # return을 만나는 순간 즉시 종료됩니다. 리턴이후에 코드를 써도 절대 실행안됩니다.
    a = 10

def sub(n1, n2):
    res = n1 - n2
    return res

def multi(n1, n2):
    print(f'{n1} x {n2} = {n1 * n2}')

def infinite_loop():
    while True:
        msg = int(input('>>> '))

        if msg == 0:
            print('break!!')
            break   # 브레이크는 반복문 종료
        elif msg == 1:
            print('continue!!')
            continue
        elif msg == 2:
            print('return!')
            return    # 리턴은 함수종료
        print('하하호호')
    print('함수 이제 끝남')



def operate_all(n1, n2):
    # return [n1+n2, n1-n2, n1*n2, n1/n2]
    return {
        'add': add(n1,n2)
        , 'sub': sub(n1,n2)
        , 'mul': n1 * n2
        , 'div': n1 / n2
    }




#########################################################
# 실행부

if __name__== '__main__':
    
    print(add(10, 5))

    result = add(100, 200)
    print(result)

    result2 = sub(100, 20)
    print(result2)

    multi(3, 7)

    result3 = add(add(add(2, 3), 8), 11)
    print(result3) 

    add(sub(10, 10), sub(20,10))
    
    # add(multi(10, 10), sub(20,10)) multi에는 리턴이없으므로 안되는 식
    multi(add(4, 7), sub(10,4)) # 멀티로 시작하므로 가능한 식

    print('='*40)

    # infinite_loop()

    result_list = operate_all(10,5)
    print(result_list)
    print(result_list['mul'])