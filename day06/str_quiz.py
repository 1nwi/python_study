

ssn = input('주민번호: ')
# 123456-1234567
genderNum = int(ssn[7])



year = int(ssn[:2])
mon = int(ssn[2:4])
day = int(ssn[4:6])
front = int(ssn[:6])
back = int(ssn[7:])

born = 1900 + year
age = 2022 - born


if genderNum == 1 or genderNum == 3:
    if genderNum == 3:
        born2 = 2000 + year
    print(f'주민번호 앞자리: {front}')
    print(f'주민번호 뒷자리: {back}')
    print(f'{born}년생 {mon}월 {day}일 {age}세 남성입니다.')
elif genderNum == 2 or genderNum == 4:
    print(f'주민번호 앞자리: {front}')
    print(f'주민번호 뒷자리: {back}')
    print(f'{born}년생 {mon}월 {day}일 {age}세 여성입니다.')
else:
    print('외국인입니다.')

  