from Stack import Stack

class Stack_Queue:

    def __init__(self):
        self.stack_top = Stack()
        self.stack_bottom = Stack()

    def dequeue(self):
        while self.stack_top.isEmpty() == False:
            self.stack_bottom.push(self.stack_top.pop())
        self.stack_top.pop()
        while self.stack.bottom.isEmpty() == False:
            self.stack_top.push(self.stack_top.pop())

    def enqueue(self, node):
        self.stack_top.push(node)

    def isEmpty(self):
        return self.stack_top.isEmpty()

    def size(self):
        return self.stack_top.size()

    def peek(self):
        return self.stack_top.peek()