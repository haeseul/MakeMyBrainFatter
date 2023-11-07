M = 13  # 버킷 크기
table = [0] * M

def hashFn(key):
    return key % M

def hashFn2(key):
    return 11 - (key % 11)

def getLinear(v, i):
    return (v + i) % M
def getQuadratic(v, i):
    return (v + i*i) % M
def getDouble(v, i, key):
    return (v + i * hashFn2(key)) % M
def insert(key):
    v = hashFn(key)
    i = 0
    while i < M:
        b = getLinear(v, i)     # 버킷 조사
        # b = getQuadratic(v, i)
        # b = getDouble(v, i, key)    # 이중 해싱

        if table[b] == 0:
            table[b] = key
            return
        else:
            i += 1

def search(key):
    v = hashFn(key)
    i = 0
    while i < M:
        b = getLinear(v, i)  # 버킷 조사
        # b = getQuadratic(v, i)
        # b = getDouble(v, i, key)    # 이중 해싱

        print('[%d] ' % table[b], end='')
        if table[b] == 0:
            return 0
        elif table[b] == key:
            return table[b]
        else:
            i += 1

def delete(key):
    v = hashFn(key)
    i = 0
    while i < M:
        b = getLinear(v, i)  # 버킷 조사
        # b = getQuadratic(v, i)
        # b = getDouble(v, i, key)    # 이중 해싱

        print('[%d] ' % table[b], end='')
        if table[b] == 0:
            print('No key to delete')
            return 0
        elif table[b] == key:
            table[b] = -1       # 0으로 초기화가 아니라, 있다가 없어진 값이라는 걸 표현해줘야 함
            return
        else:
            i += 1

def display():
    print(); print('Bucket   Key'); print('=============')
    for i in range(M):
        print('HT[%2d] :  %2d' %(i, table[i]))


if __name__ == '__main__':
    data = [45, 27, 88, 9, 71, 60, 46, 38, 24]
    for d in data:
        print("h(%2d) = %2d" %(d, hashFn(d)), end=' ')
        insert(d)
        print(table)

    display()
    print(); print('Search (46) -->', search(46))
    print('Search (39) -->', search(39))
    delete(60); print()
    delete(46); print(); display()
    print('Search (24) -->', search(24))
