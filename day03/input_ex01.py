

print('='*40)

name = input("당신의 이름: ")
# age = input('당신의 나이: ')
age = int(input('당신의 나이: '))
# print(f'age의 타입: {type(age)}') // age의 타입: <class 'int'>


print('='*40)
print(f'{name}님 환영합니다!!!')
print('당신은 {}세이군요!'.format(age))

# print(f'age의 타입: {type(age)}') // age의 타입: <class 'str'>


# input은 입력값을 무조건 str타입으로 처리합니다.
print('당신은 {}년생이군요!'.format(2021-age+1))