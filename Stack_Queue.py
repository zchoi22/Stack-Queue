from Stack import Stack

class Stack_Queue:

    def __init__(self):
        self.stack_top = Stack()
        self.stack_bottom = Stack()

    #dequeue moves all elements in a stack to the other one,
    #pops the top elements, and moves then back to imitate a first in last out
    def dequeue(self):
        while self.stack_top.isEmpty() == False:
            self.stack_bottom.push(self.stack_top.pop())
        self.stack_top.pop()
        while self.stack.bottom.isEmpty() == False:
            self.stack_top.push(self.stack_top.pop())

    #relies on the top stack, simply pushes new node on top
    def enqueue(self, node):
        self.stack_top.push(node)

    #again, relies on top stack, same for size and peek
    def isEmpty(self):
        return self.stack_top.isEmpty()

    def size(self):
        return self.stack_top.size()

    def peek(self):
        return self.stack_top.peek()