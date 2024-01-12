for x in [1, 2, 3, 4]:
    print(x)
else:
    print('출력 완료')

print('----------------')

for x in [1,2,3,4]:
    if x%3:
        print(x)
    else:
        break
else:
    print('출력 완료')

print('----------------')

cnt = 5
while cnt>0:
    print(cnt)
    cnt -= 1
    if input()=='중단':
        break
else:
    print('발사!')
