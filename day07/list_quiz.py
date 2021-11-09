

print('# 먹고 싶은 음식을 입력하세요~~')
print('[그만 입력하려면 \'배불러\'라고 입력하세요.]')


food_list = []
while True:
    food_name = input('> ')
    if food_name == '배불러':
        break
    #음식 이름을 리스트에 저장
    food_list.append(food_name)

print('입력을 종료합니다.')
print(f'내가 먹고싶은 음식: {food_list}')