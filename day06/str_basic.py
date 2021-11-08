


#  자바나 스크립트는 (" ") 만 먹히지만 파이썬은 (""), ('')둘다 먹히지만 ('')를 씁니다

s1 = "안녕"
print(type(s1))



s2 = '잘가'
print(type(s2))


#  (" ") 안에 (" ")가 또있으면 오류가 납니다.
s3 = '나는 홍길동에게 "도와줘"라고 말했다.'
s4 = "Let's go!"
s5 = "나는 홍길동에게 \"도와줘\"라고 말했다."
print(s5)

# 자바나 스크립트는 이렇게 씁니다 
# s5 = "나는 홍길동에게 \"도와줘\"라고 말했다."

# \를 특수부호로 만들기위해서는 역슬래시를 1번더 씁니다.
file_path = 'c:\\temp\\new.png'
print(file_path)


#  ''' '''으로 여러줄을 프린트할수있음 
lyrice ='''Baby 네게 반해버린 내게 왜 이래
두렵다고 물러서지 말고
그냥 내게 맡겨봐라 어때 My lady

Ring Ding Dong Ring Ding Dong
Ring Diggi Ding Diggi Ding Ding Ding
Ring Ding Dong Ring Ding Dong
Ring Diggi Ding Diggi Ding Ding Ding

Ring Ding Dong Ring Ding Dong
Ring Diggi Ding Diggi Ding Ding Ding
Ring Ding Dong Ring Ding Dong
Ring Diggi Ding Diggi Ding Ding Ding'''
print(lyrice)