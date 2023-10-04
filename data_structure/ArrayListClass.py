class ArrayList:

    def __init__(self, capacity = 100):
        self.capacity = capacity
        self.array = [None] * self.capacity
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity

    def insert(self, pos, e):
        if not self.isFull() and 0 <= pos <= self.size:
            for i in range(self.size, pos, -1):
                self.array[i] = self.array[i - 1]
            self.array[pos] = e
            self.size += 1
        else:
            print("Overflow or Invalid Position")

    def replace(self, pos, e):
        if 0 <= pos < self.size:
            self.array[pos] = e
        else: pass

    def getEntry(self, pos):
        if 0 <= pos < self.size:
            return self.array[pos]
        else: return None

    def delete(self, pos):
        if not self.isEmpty() and 0 <= pos < self.size:
            e = self.array[pos]
            for i in range(pos, self.size - 1):
                self.array[i] = self.array[i + 1]
            self.size -= 1
            return e
        else:
            print("Underflow of Invalid Position")

    def display(self):
        for i in range(self.size):
            print(self.array[i], end=' ')
        print()

if __name__ == "__main__":
    L1 = ArrayList(10)
    L2 = ArrayList(7)

    L1.insert(0, 10)
    L1.insert(0, 20)
    L1.insert(2, 30)

    L2.insert(0, 'A')
    L2.insert(1, 'B')
    L2.insert(0, 'C')

    L1.display()
    L2.display()

    L1.delete(0)
    L2.delete(L2.size - 1)
    L1.display()
    L2.display()
