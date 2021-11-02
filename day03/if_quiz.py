

korean = int(input('국어: '))
english = int(input('영어: '))
math = int(input('수학: '))

average = ((korean + english + math) / 3)
# average = round(average, 2) <- 영원히 반올림하는 방법
print('당신의 평균점수: {:.2f} 점'.format(average)) #여기서만 반올림

if average >= 60:
    print('이번 시험에 통과하셨습니다.')
else:
    print('재수강 대상자입니다.')
print('열공하세요!')    

