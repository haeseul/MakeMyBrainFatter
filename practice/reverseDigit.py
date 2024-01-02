num = 358

rem = rev = 0

while num >= 1:
    rem = num % 10          # 8  5  3
    rev = rev * 10 + rem    # 8  85 853
    num //= 10              # 35 3  0

print(rev)