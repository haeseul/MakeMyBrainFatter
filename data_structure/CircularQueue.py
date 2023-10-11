class CircularQueue:

    def __init__(self, capacity = 8):
        self.capacity = capacity
        self.queue = [None] * self.capacity
        self.front = self.rear = 0

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return self.front == (self.rear + 1) % self.capacity

    def enqueue(self, e):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.capacity
            self.queue[self.rear] = e
        else:
            print('FULL')

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            return self.queue[self.front]
        else:
            print('EMPTY')

    def peek(self):
        if not self.isEmpty():
            return self.queue[(self.front + 1) % self.capacity]
        else:
            print('EMPTY')

    def display(self):
        print('Front : %d, Rear : %d' %(self.front, self.rear))

        i = self.front

        while i != self.rear:
            i = (i+1) % self.capacity
            print('[%c] ' %self.queue[i], end=' ')
        print()

if __name__ == '__main__':
    q = CircularQueue()
    q.enqueue('A')
    q.enqueue('B')
    q.enqueue('C')
    q.enqueue('D')
    q.enqueue('E')
    q.display()

    print('Dequeue --> ', q.dequeue())
    print('Dequeue --> ', q.dequeue())
    print('Dequeue --> ', q.dequeue())
    q.display()

    q.enqueue('A')
    q.enqueue('B')
    q.enqueue('C')
    q.display()
