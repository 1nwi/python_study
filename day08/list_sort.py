

nums = [144, 32, 33 , 99, 22, 100, 255]
print(nums)

nums.sort()
print(nums)

print('=' * 40)

nums2 = [10,9,8,7,6,5,4,3,2,1]
nums2.reverse()
print(nums2)


nums = [144, 32, 33 , 99, 22, 100, 255]
# nums.sort()    
# nums.reverse()

nums.sort(reverse=True) #내림차 정렬
print(nums) 

print('=' * 40)

# 이번주 로또번호를 생성해서 오름차정렬해서 출력하세요.


import random  # 수업진행상 여기다 적지만 원래는 1번째줄에 쓰는게 정석

lotto = []
while len(lotto) < 6:
    lotto_num = random.randint(1, 45)

    if lotto_num not in lotto:
    # 중복이 아닐 경우에만
        lotto.append(lotto_num)

lotto.sort()
print(lotto)