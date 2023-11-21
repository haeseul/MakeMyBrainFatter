n = 100

class MaxHeap:
    def __init__(self):
        self.heap = [None]*n
        self.heapSize = 0    # 노드개수, 노드번호, 노드인덱스, 가장 마지막에 입력된 인덱스

    def upHeap(self):
        idx = self.heapSize
        item = self.heap[idx]

        # Root 가 아니고 부모보다 크다면
        while idx != 1 and item > self.heap[idx//2]:
            self.heap[idx] = self.heap[idx//2]
            idx //= 2

        self.heap[idx] = item

    def insertItem(self, item):
        self.heapSize += 1
        self.heap[self.heapSize] = item
        self.upHeap()

    def downHeap(self):
        item = self.heap[1]
        parent = 1
        child = 2

        # 비교할 자식 노드가 없어질 떄까지
        while child <= self.heapSize:
            # 오른쪽 노드가 있다면 왼쪽(child), 오른쪽(child+1) 먼저 비교
            if child < self.heapSize and self.heap[child+1] > self.heap[child]:
                child += 1
            if item >= self.heap[child]:
                break
            self.heap[parent] = self.heap[child]
            parent = child
            child *= 2      # 자식의 왼쪽 노드로 이동
        self.heap[parent] = item

    def deleteItem(self):
        item = self.heap[1]     # 삭제대상 : root
        self.heap[1] = self.heap[self.heapSize]
        self.heapSize -= 1
        self.downHeap()
        return item

    def display(self):
        print('Heap : ', self.heap[1:self.heapSize+1])

if __name__ == '__main__':
    h = MaxHeap()
    data = [7,5,3,9,4,6,2,2,1,3]
    for e in data:
        h.insertItem(e)
        h.display()
    # h.insertItem(8)
    # h.display()

    print('[%d] is deleted' % h.deleteItem())
    h.display()