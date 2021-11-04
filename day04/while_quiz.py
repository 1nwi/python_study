
# ****복습필수****
# x ~ y 까지의 총합
#n = 1   # x = 1

#while n <= 10:   # y = 10
#    total_two += n
#    n += 1


x = int(input('정수 1: '))
y = int(input('정수 2: '))

total = 0
n = x

while n <= y:
    total += n
    n += 1
print(f'{x}~{y}까지의 총합: {total}')