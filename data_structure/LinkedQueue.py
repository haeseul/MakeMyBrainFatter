class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next    # 다음 것의 주소, 처음엔 next 결정X

class QueueType():
    def __init__(self):
        self.tail = None
        self.size = 0

    def isEmpty(self):
        return self.tail is None
        # or return self.size == 0

    def enqueue(self, data):    # insertLast()
        node = Node(data)
        if self.isEmpty():          # 큐가 공백이라면 내가 처음이자 마지막
            node.next = node        # 내가 가리키는 곳 = 나 자신
            self.tail = node        # 나를 가리키는 곳 = tail이 나를 가리킴
        else:
            node.next = self.tail.next  # 내가 가리키는 곳
            self.tail.next = node   # 나를 가리키는 곳 (마지막 노드의 오른쪽에 내가 들어감)
            self.tail = node        # 내가 전체 리스트의 마지막이 됨
        self.size += 1

    def insertFirst(self, data):
        node = Node(data)
        if self.isEmpty():
            node.next = node
            self.tail = node
        else:
            node.next = self.tail.next
            self.tail.next = node
            # insertLast와의 차이점 : 맨 앞에 추가하기 때문에 내가 마지막이 될 필요가 없음
        self.size += 1

    def dequeue(self):      # deleteFirst()
        if not self.isEmpty():
            p = self.tail   # 맨 뒤 포인터
            q = p.next      # 맨 앞 포인터 (노드가 하나여도 자기 자신을 가리키기 때문에 괜찮음)
            data = q.data

            if p == q:      # 노드가 1개일 때
                # 삭제될 노드 1개만 있을 때 (처음이자 마지막 노드일 때)
                #   => 삭제 후 전체 리스트가 Empty가 되어야 해서 init 해야 함
                self.tail = None
            else:
                p.next = q.next     # 맨 뒤를 맨 앞에 연결만 해주면 됨
            self.size -= 1
            return data
        else: pass

    def display(self):
        if not self.isEmpty():
            p = self.tail.next      # tail을 가리키는 포인터
            for i in range(self.size):
                print('[%s] -> ' % p.data, end='')
                p = p.next
            print('\b\b\b    ')
        else: pass


if __name__ == '__main__':
    q = QueueType()
    q.enqueue('A')
    q.display()
    q.enqueue('C')
    q.display()
    q.enqueue('B')
    q.display()

    q.insertFirst('D')
    q.display()

    q.dequeue()
    q.display()