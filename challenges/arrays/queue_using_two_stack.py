"""
A queue is an abstract data type that maintains the order in which elements were added to it, allowing the oldest elements to be removed from the front and new elements to be added to the rear. This is called a First-In-First-Out (FIFO) data structure because the first element added to the queue (i.e., the one that has been waiting the longest) is always the first one to be removed.

A basic queue has the following operations:

Enqueue: add a new element to the end of the queue.
Dequeue: remove the element from the front of the queue and return it.
In this challenge, you must first implement a queue using two stacks. Then process q queries, where each query is one of the following 3 types:

1 x: Enqueue element x into the end of the queue.
2: Dequeue the element at the front of the queue.
3: Print the element at the front of the queue.
"""

class Queue():
    def __init__(self) -> None:
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, data):
        self.in_stack.append(data)

    def dequeue(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()
    
    def __str__(self):
        if not self.out_stack:
            return str(self.in_stack[0])
        else:
            return str(self.out_stack[-1])

if __name__ == '__main__':
    queue = Queue()
    q = int(input())
    for i in range(q):
        e = list(map(int, input().split()))
        if e[0] == 1:
            queue.enqueue(e[1])
        elif e[0] == 2:
            queue.dequeue()
        elif e[0] == 3:
            print(queue)
            continue

    """x = Queue()
    x.enqueue(5)
    x.enqueue(6)
    x.enqueue(7)
    print(x.in_stack)
    x.dequeue()
    print(x.in_stack)
    print(x.out_stack)
    x.dequeue()
    print(x.out_stack)
    x.enqueue(8)
    x.enqueue(9)
    x.dequeue()
    x.dequeue()"""