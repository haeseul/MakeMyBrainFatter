def printStep(a, idx):
    print('    Step %d : '% idx, end='')
    print(a)

def selectionSort(a):
    n = len(a)

    for i in range(n-1):
        least = i
        for j in range(i+1, n):
            if a[j] < a[least]:
                least = j
        a[i], a[least] = a[least], a[i]
        printStep(a, i+1)

def insertionSort(a):
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i-1
        while j>=0 and a[j]>key:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
        printStep(a, i)

def bubbleSort(a):
    n = len(a)
    for i in range(n-1, 0, -1):
        flag = False
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                flag = True
        if not flag:
            break
        printStep(a, n-i)

if __name__ == "__main__":
    data = [5,3,8,4,9,1,6,2,7]
    L = list(data)
    print("Before : ", L)
    selectionSort(L)
    print()

    L = list(data)
    print("Before : ", L)
    insertionSort(L)
    print()

    L = list(data)
    print("Before : ", L)
    bubbleSort(L)
    print()
