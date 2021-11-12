
'''
x = input('>> ').split()
for i in range(len(x)):
    x[i] = int(x[i])
print(x)
'''

# 위 아래 같은거 

x = list(map(int, input(''>> '').split()))
print(x)