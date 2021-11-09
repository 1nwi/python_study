
tvxq = ['영웅재중', '최강창민', '유노윤호', '시아준수', '믹키유천']
print('\n삭제전', tvxq)

while True:
    print('삭제할 이름을 입력하세요!')
    old_name = input('> ')

    if old_name in tvxq:
        tvxq.remove(f'{old_name}')
        print('삭제후: ', tvxq)
        break

    else:
        print(f'{old_name}는(은) 없는 멤버입니다.')