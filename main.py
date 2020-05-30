import os
print (os.getcwd())
from Modules.DataStructures import stack, queue

new_stack = stack([1, 2, 3])
new_stack.checkStack()

print (new_stack.pop())

new_queue = queue([1, 2, 3])

new_queue.queue.checkQueue()
new_queue.dequeue()