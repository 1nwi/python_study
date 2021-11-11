

print('[영어 단어장 만들기]')
print('- 종료하시려면 영단어에 "그만"을 입력하세요!')

eng_kor = {}

while True:
    eng = input('영단어: ')
    if eng == '그만':
        break
    elif eng == eng_kor:
        print('이미 등록된 단어입니다.')
    else:
        kor = input('뜻: ')
        if kor not in eng_kor:
            eng_kor[eng] = kor

print('종료합니다')
print('\n*** 단어장 ***')
print('-' * 30)

print(eng_kor)