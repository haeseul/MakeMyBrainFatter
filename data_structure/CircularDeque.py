from CircularQueue import CircularQueue

class CircularDeque(CircularQueue):
    def __init__(self, capacity=10):
        super().__init__(capacity)  # 자식 생성 전 부모 생성해야 함

    # isEmpty(), isFull(), display()...

    def addFront(self, e):
        if not self.isFull():
            self.queue[self.front] = e
            self.front = (self.front - 1 + self.capacity) % self.capacity
        else: pass

    def addRear(self, e):
        self.enqueue(e)

    def deleteFront(self):
        self.dequeue()

    def deleteRear(self):
        if not self.isEmpty():
            e = self.queue[self.rear]
            self.rear = (self.rear - 1 + self.capacity) % self.capacity
            return e
        else: pass

    def getFront(self):
        self.peek()

    def getRear(self):
        if not self.isEmpty():
            return self.queue[self.rear]
        else: pass

if __name__ == '__main__':
    import random

    d = CircularDeque()
    for i in range(4):
        d.addFront(random.randint(65, 90))  # a~z 난수생성
    d.display()

    for i in range(3):
        d.addRear(random.randint(65, 90))
    d.display()

    for i in range(2):
        d.deleteFront()
    d.display()

    for i in range(2):
        d.deleteRear()
    d.display()