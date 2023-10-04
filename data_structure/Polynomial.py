class Polynomial:

    def __init__(self, capacity=100):
        self.capacity = capacity
        self.array = [None] * self.capacity
        self.deg = [None] * self.capacity
        self.size = 0

    def degree(self):
        for i in range(self.size):
            self.deg[i] = i
            i += 1
        self.array = self.array[0:self.size]
        self.deg = self.deg[0:self.size]

    def eval(self, scalar):
        sum = 0
        for i in range(1, self.size):
            tmp = 1
            tmp *= self.array[i]
            for j in range(self.deg[i]):
                tmp *= scalar
            sum += tmp
        sum += self.array[0]
        return sum

    def add(self, other):
        c = Polynomial()
        if self.size > other.size:
            c.size = self.size
            for i in range(self.size):
                c.array[i] = self.array[i]
            for i in range(other.size):
                c.array[i] = self.array[i] + other.array[i]
        else:
            c.size = other.size
            for i in range(other.size):
                c.array[i] = other.array[i]
            for i in range(self.size):
                c.array[i] = self.array[i] + other.array[i]
        c.degree()
        return c

    def read(self):
        nums = list(map(int, input('Input degrees in order : ').split()))
        for i in range(len(nums)):
            self.array[i] = nums[len(nums)-1-i]
            self.size += 1
        self.degree()

    def display(self, s):
        print(s, end='')
        for i in range(self.size-1, 0, -1):
            print(f"{self.array[i]}x^{self.deg[i]} + ", end='')
        print(self.array[0])

if __name__ == "__main__":
    a = Polynomial()
    b = Polynomial()

    a.read()
    b.read()
    c = a.add(b)

    a.display("A(x) = ")
    b.display("B(x) = ")
    c.display("C(x) = ")

    print("C(2) = ", c.eval(2))