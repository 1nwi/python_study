

s = 'python'

# 0부터 시작
print(s)
print(s[2])
print(s[4])
# print(s[7])    << 범위벗어나면 오류납니다

# 뒤에서 샐때는 -로 // 뒤에서 -1부터 시작
print(s[-5])
print(s[-5] == s[1])

# 문자열은 for문에서 사용할 수 있는 자료형입니다.
print('=' * 40)

for c in s:
    print(c + '!!!')


print('# 주민번호를 입력하세요. ex)99111-1234567')
ssn = input('> ')

genderNum = int(ssn[7])

if genderNum == 1 or genderNum == 3:
    print('남성입니다.')
elif genderNum == 2 or genderNum == 4:
    print('여성입니다.')
else:
    print('외국인입니다.')