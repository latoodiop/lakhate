class MyEmptyStackException(Exception):
    pass

class MyOutOfSizeException(Exception):
    pass

class MyStackNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyStack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.top = None
        self.size = 0

    def add_to_stack(self, item):
        if self.is_full():
            raise MyOutOfSizeException("Stack is full")
        node = MyStackNode(item)
        node.next = self.top
        self.top = node
        self.size += 1

    def pop_from_stack(self):
        if self.is_empty():
            raise MyEmptyStackException("Stack is empty")
        item = self.top.data
        self.top = self.top.next
        self.size -= 1
        return item

    def is_full(self):
        return self.size == self.max_size

    def is_empty(self):
        return self.size == 0

# Exemple d'utilisation :
stack = MyStack(5)
print(stack.is_empty())  # True
stack.add_to_stack(1)
stack.add_to_stack(2)
stack.add_to_stack(3)
print(stack.is_empty())  # False
print(stack.is_full())   # False
print(stack.pop_from_stack())  # 3
print(stack.pop_from_stack())  # 2
print(stack.pop_from_stack())  # 1
print(stack.is_empty())  # True
print(stack.is_full())   # False