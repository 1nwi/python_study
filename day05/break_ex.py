

for a in range(10):
    if a == 5: break
    print(a, end=' ')
print('\n반복문 종료!')

# print가 break의 위아래 위치에 따라서 출력되는게 다름  

n = 1
while n <= 100:
    print(n, end=' ')
    if n == 9:
        print('\n박복문 끝!')
        break
    n += 1