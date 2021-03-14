# The functions associated with stack are: empty(), size(), top(), push(element), pop()
# Stack in Python can be implemented using following ways: 
# list
# collections.deque
# queue.LifoQueue

# using list

# stack = []

# stack.append(1)
# stack.append(100)

# print(stack.pop())
# print(stack)

# using deque -- prefered
# O(1) time complexity for append and pop operations as compared to list which provides O(n) time complexity. 

# from collections import deque

# stack = deque()

# stack.append(12)
# stack.append(133)
# stack.append(90)

# stack.pop()
# print(stack)

# or we can basically using queue LIFO which is a stack implementation
