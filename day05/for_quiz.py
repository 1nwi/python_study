
# while과 for 을 이용한 구구단만들기


x = int(input('구구단 단수: '))

print(f'구구단 {x} 단')
print('='* 30)

for n in range(1, 10):
    print(f'{x} x {n} = {x * n}')







y = int(input('구구단 단수: '))

print(f'구구단 {y} 단')
print('=' * 30)

n = 1
while n <= 9:
    print(f'{y} x {n} = {y * n}')
    n += 1

