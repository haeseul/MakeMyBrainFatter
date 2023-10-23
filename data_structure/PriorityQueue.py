class PriorityQueue:
    def __init__(self, capa=10):
        self.capa = capa
        self.queue = [None] * capa
        self.size = 0  # 요소개수

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capa - 1

    def display(self):
        print(self.queue[:self.size])

    def findMaxIndex(self):
        if self.isEmpty():
            max = -1  # Empty
        else:
            max = 0
            for i in range(self.size):
                if self.queue[i] > self.queue[max]:
                    max = i
        return max

    def enqueue(self, e):
        if not self.isFull():
            self.queue[self.size] = e
            self.size += 1

    def dequeue(self):
        highest = self.findMaxIndex()
        if highest != -1:  # if not Empty
            self.size -= 1  # priority를 맨 뒤로 보내서 size index와 일치시키기
            self.queue[highest], self.queue[self.size] = self.queue[self.size], self.queue[highest]
            return self.queue[self.size]

    def peek(self):
        highest = self.findMaxIndex()
        if highest != -1:
            return self.queue[highest]

if __name__ == '__main__':
    p = PriorityQueue()
    p.enqueue(34)
    p.enqueue(18)
    p.enqueue(27)
    p.enqueue(45)
    p.enqueue(15)
    p.display()
    while not p.isEmpty():
        print('Max Priority =', p.dequeue())