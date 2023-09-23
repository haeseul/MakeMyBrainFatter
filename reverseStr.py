def reverse_str(a):
    if len(a) < 1:
        return a
    else:
        return reverse_str(a[1:])+a[0]

if __name__ == "__main__":
    numTestCases = int(input())
    for i in range(numTestCases):
        print(reverse_str(input()))