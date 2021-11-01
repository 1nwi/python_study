
name = "홍길동"
score = 78

# score타입은 int , name타입은 str 이라서 + 가 error뜸
# print안에 socre 앞에 str을 넣어줌
print(name + "님의 점수는 " + str(score) + "점입니다.")

print(type(score))

n1 = 10
n2 = '34'
print(str(n1) + n2)
print(n1 + int(n2))

# 타입 변환 함수는 일시적 변화일 뿐 실제값은 변하지않는다.
print('==========================')

print(type(n2))

n2 = int(n2)
print(type(n2))

# 변환대상이 정수로 바뀔 수 없는 값이면 에러 발생
# int('hello')

s = '2.33'
print(float(s))

# 반올림할 때는 round() 함수를 사용
print('=============================')

print(round(4.78))
print(int(4.78))  # 소수점 버림
print(round(4.18))
print(round(4.67812345544333, 2)) # (round(4.xxxx, 자릿수))
