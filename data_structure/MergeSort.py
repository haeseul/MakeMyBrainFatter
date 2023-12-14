data = [5,3,8,4,9,1,6,2,7]
sorted = [0] * len(data)    # sorted 원소를 저장할 임시배열

def merge(left, mid, right):
    i = left        # 왼쪽 분할 리스트의 첫 번째
    j = mid + 1     # 오른쪽 분할 리스트의 첫 번째
    k = left        # sorted 배열의 index

    while i <= mid and j <= right:
        if data[i] <= data[j]:
            sorted[k] = i
            i += 1
            k += 1
        else:
            sorted[k] = j
            j += 1
            k += 1

    # Flushing
    if i > mid:     # 오른쪽 분할 리스트에 남은 게 있는 경우
        for l in range(j, right+1):
            sorted[k] = data[l]
            k += 1
    else:       # 왼쪽 분할 리스트에 남은 게 있는 경우
        for l in range(i, mid+1):
            sorted[k] = data[l]
            k += 1

    # left, right 두 개만 change (10, 27 -> 27, 10)
    data[left:right+1] = sorted[left:right+1]

def mergeSort(left, right):
    if left < right:
        mid = (left + right) // 2
        mergeSort(left, mid)
        mergeSort(mid+1, right)
        merge(left, mid, right)

if __name__ == '__main__':
    print('Origin : ', data)
    mergeSort(0, len(data)-1)
    print('Sorted : ', data)