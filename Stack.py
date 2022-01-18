from Node import Node

class Stack:

    def __init__(self, *args):
        if len(args) == 1:
            self.root = args[0]
        else:
            self.root = None
        self.size = 0

    def push(self, root):
        if self.isEmpty():
            self.root = root
        else:
            self.root.set_prev(root)
            root.set_next(self.root)
            self.root = root
        self.size+=1

    def pop(self):
        self.root.get_next().set_prev(None)
        temp = self.root
        self.root = self.root.get_next()
        self.size-=1
        return temp

    def isEmpty(self):
        return self.size == 0

    def size(self):
        return self.size()

    def peek(self):
        return self.root