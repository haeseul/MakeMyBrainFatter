min, max = map(int, input().split())

while True:
    b = int(input())
    if min <= b <= max:
        print('Nothing to report')
    elif b == -999:
        break
    else:
        print('Alert!')
        break