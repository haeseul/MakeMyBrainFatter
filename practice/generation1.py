a = int(input('What year were you born? '))
b = None
if a < 1925:
    b = 'The Greatest Generation'
elif a < 1946:
    b = 'The Silent Generation'
elif a < 1965:
    b = 'Baby Boomer'
elif a < 1981:
    b = 'Generation X'
elif a < 1997:
    b = 'Millennial'
else:
    b = 'Generation Z'

print(f"You're {b}")