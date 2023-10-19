class DNode:
    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next

class DListType():
    def __init__(self):
        self.front = None   # Deque
        self.rear = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0   # or self.front is None or self.rear is None

    def addFront(self, data):   # InsertFirt()
        node = DNode(data, None, self.front)

        if self.isEmpty():
            self.front = self.rear = node
        else:
            # 가리키는 순서 중요!!
            self.front.prev = node      # 내 오른쪽이 먼저 나를 가리킴
            self.front = node           # 내 왼쪽에서 나를 가리킴
        self.size += 1

    def addRear(self, data):    # InsertLast()
        node = DNode(data, self.rear, None)

        if self.isEmpty():
            self.front = self.rear = node
        else:
            # 가리키는 순서 중요!!
            self.rear.next = node  # 내 왼쪽에서 먼저 나를 가리킴
            self.rear = node  # 내 오른쪽이 나를 가리킴
        self.size += 1

    def add(self, pos, data):     # 중간에 넣기
        node = DNode(data, None, None)  # 내 앞뒤에 뭐가 올지 모름

        if pos == 1:
            self.addFront(data)
        elif pos == self.size + 1:  # 맨 마지막에 들어갈 때
            self.addRear(data)
        else:
            p = self.front

            for i in range(1, pos):
                p = p.next

            node.prev = p.prev      # 내가 가리키는 곳
            node.next = p           # 내가 가리키는 곳
            p.prev.next = node      # 나를 가리키는 곳
            p.next = node           # 나를 가리키는 곳

        self.size += 1


    def display(self):
        if not self.isEmpty():
            p = self.front    # 포인터 변수

            while p is not None:
                print('[%s] -> ' % p.data, end='')
                p = p.next
            print('\b\b\b    ')
        else: pass

if __name__ == '__main__':
    dl = DListType()
    dl.addFront('A')
    dl.addFront('C')
    dl.addFront('D')
    dl.display()

    dl.addRear('E')
    dl.display()