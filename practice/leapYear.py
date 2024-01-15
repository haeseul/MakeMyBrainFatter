a = int(input())
b = False

if a % 4 == 0:
    if a % 100 == 0:
        if a % 400 == 0:
            b = True
    else:
        b = True

if b:
    print(f"출력 연도 {a}년은 윤년입니다.")
else:
    print(f"출력 연도 {a}년은 평년입니다.")
