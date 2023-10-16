import queue

q = queue.Queue(maxsize=20)

for v in range(1, 10):
    q.put(v)
print('Queue : ', end='')

for _ in range(1, 10):
    print(q.get(), end=' ')
print()


s = queue.LifoQueue(maxsize=20)

for v in range(1, 10):
    s.put(v)
print('Stack : ', end='')

for _ in range(1, 10):
    print(s.get(), end=' ')
print()