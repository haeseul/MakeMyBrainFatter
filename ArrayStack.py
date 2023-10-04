class ArrayStack:

    def __init__(self, capacity = 100):
        self.capacity = capacity
        self.stack = [None] * self.capacity
        self.top = -1

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.capacity - 1

    def push(self, e):
        if not self.isFull():
            self.top += 1
            self.stack[self.top] = e
        else:
            print('Overflow!')

    def pop(self):
        if not self.isEmpty():
            e = self.stack[self.top]
            self.top -= 1
            return e
        else:
            print('Empty!')

    def peek(self):
        if not self.isEmpty():
            return self.stack[self.top]
        else:
            print('Empty!')

    def size(self):
        return self.top + 1

    def display(self):
        print(self.stack[self.top::-1])

if __name__ == '__main__':
    s = ArrayStack()

    str = input('Input a string : ')

    for c in str:
        s.push(c)
    # s.display()

    # print('After Pop : %c' %s.pop())
    # s.display()
    # print('After Peek : %c' %s.peek())
    # s.display()

    # 데이터가 스택에 들어왔다가 바로 빠져나올
    while not s.isEmpty():
        print(s.pop(), end='')