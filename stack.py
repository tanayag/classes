class Stack:
    def __init__(self):
        self.items=[]
    def __str__(self):
        return str(self.items)
    def show(self):
        print str(self.items)
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def size(self):
        return len(self.items)
    def __repr__(self):
        return str(self.items)
