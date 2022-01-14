class Node:

    def __init__(self, *args):
        if len(args) == 1:
            self.data = args[0]
            self.prev = None
            self.next = None
        elif len(args) == 3:
            self.data = args[0]
            self.prev = args[1]
            self.next = args[2]
        else:
            self.data = None
            self.prev = None
            self.next = None

    def get_data(self):
        return self.data

    def get_prev(self):
        return self.prev

    def get_next(self):
        return self.next

    def set_data(self, data):
        self.data = data

    def set_next(self, next):
        self.next = next

    def set_prev(self, prev):
        self.prev = prev

    def toString(self):
        return "Node: " + self.data