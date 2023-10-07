def permuteString(str, begin, end):
    gap = end - begin
    if gap == 1:
        print(str)
    else:
        for i in range(gap):
            str[begin], str[begin+i] = str[begin+i], str[begin]
            permuteString(str, begin+i, end)
            str[begin], str[begin+i] = str[begin+i], str[begin]


if __name__ == '__main__':
    str = list('abcd')
    print(str)

    # permuteString(str, 0, len(str))