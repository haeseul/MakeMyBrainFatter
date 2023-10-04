class ArraySet:

    def __init__(self, capacity = 100):
        self.capacity = capacity
        self.array = [None] * self.capacity
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity

    def display(self):
        for i in range(self.size):
            print(self.array[i], end=' ')
        print()

    def contains(self, e):
        for i in range(self.size):
            if self.array[i] == e:
                return True
        return False

    def insert(self, e):
        if not self.contains(e) and not self.isFull():
            self.array[self.size] = e
            self.size += 1

    def delete(self, e):
        for i in range(self.size):
            if self.array[i] == e:
                # 맨 뒤의 원소를 삭제할 원소 위치로 옮기기
                self.array[i] = self.array[self.size - 1]
                self.size -= 1
                return

    def union(self, setB):
        setC = ArraySet()
        for i in range(self.size):
            setC.insert(self.array[i])
        for i in range(setB.size):
            setC.insert(setB.array[i])
        return setC

    def intersect(self, setB):
        setC = ArraySet()
        for i in range(self.size):
            if setB.contains(self.array[i]):
                setC.insert(self.array[i])
        return setC

    def difference(self, setB):
        setC = ArraySet()
        for i in range(self.size):
            if not setB.contains(self.array[i]):
                setC.insert(self.array[i])
        return setC


if __name__ == '__main__':
    s = ArraySet()
    s.insert(10)
    s.insert(30)
    s.insert(20)
    s.insert(50)
    s.display()

    t = ArraySet()
    t.insert(10)
    t.insert(40)
    t.insert(50)
    t.insert(15)
    t.display()

    s.union(t).display()
    s.intersect(t).display()
    s.difference(t).display()
