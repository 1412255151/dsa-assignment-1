class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None

    def reverse(self):
        if self.is_empty():
            return

        temp_stack = Stack()

  
        while not self.is_empty():
            temp_stack.push(self.pop())

       
        while not temp_stack.is_empty():
            self.push(temp_stack.pop())


stack_input = input("Enter the stack elements (comma-separated integers): ").split(',')
stack_input = [int(item.strip()) for item in stack_input]


stack = Stack()
for item in stack_input:
    stack.push(item)


stack.reverse()


print("Reversed stack:", stack.stack)
