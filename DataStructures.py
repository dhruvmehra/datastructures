# Stack
class stack:
    def __init__(self, initVal = []):
        self.stack = initVal
    #Pop method
    def pop(self):
        return self.stack.pop(-1)
    #push
    def push(self, value):
        self.stack.append(value)
        return self.stack
    def checkStack(self):
        print (self.stack)
    
class queue:
    def __init__(self, initVal = []):
        self.queue = initVal
    def dequeue(self):
        return self.queue.pop(0)
    def enqueue(self, value):
        self.queue.append(value)
        return (self.queue)
    def checkqueue(self):
        print (self.queue)
    def checkHead(self):
        print (self.queue[0])
    def checkTail(self):
        print (self.queue[-1])

class listNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class treeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

