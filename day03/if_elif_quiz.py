
# n%7 == 0

num = int(input('정수: '))

if num >= (num % 7) == 0:
    print('입력하신 숫자는 7의 배수입니다.')
elif num >= 0:
    print('입력하신 숫자는 0입니다.')
else:
    print('입력하신 숫자는 7의배수가 아닙니다.')