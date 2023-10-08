def nextPermutation(p):
    c = list(p)
    n = len(c) - 1

    # 최대 구간 R 찾기
    i = n - 1   # R 바로 앞 인덱스 i
    while i >= 1 and c[i] >= c[i + 1]:
        i -= 1
    if i == 0 and c[i] > c[i+1]:
        print(''.join(c[::-1]))
        return

    j = n       # R에서 가장 작은 문자 찾기
    while c[i] > c[j]:
        j -= 1

    c[i], c[j] = c[j], c[i]     # swap

    R = c[i+1:n+1][::-1]

    c = c[:i+1] + R
    c = ''.join(c)
    print(c)

if __name__ == '__main__':
    numTestCases = int(input())
    for _ in range(numTestCases):
        p = list(input().split())[1]
        nextPermutation(p)