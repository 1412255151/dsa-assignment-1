class StackWithMin:
    def __init__(self):
        self.stack = []  
        self.min_stack = [] 

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)


        if not self.min_stack or item <= self.min_stack[-1]:
            self.min_stack.append(item)

    def pop(self):
        if self.is_empty():
            return None

        item = self.stack.pop()
        
       
        if item == self.min_stack[-1]:
            self.min_stack.pop()

        return item

    def get_minimum(self):
        if not self.min_stack:
            return None
        return self.min_stack[-1]



stack_input = input("Enter the stack elements (comma-separated integers): ").split(',')
stack_input = [int(item.strip()) for item in stack_input]


stack = StackWithMin()
for item in stack_input:
    stack.push(item)


smallest_number = stack.get_minimum()


if smallest_number is not None:
    print("Smallest number in the stack:", smallest_number)
else:
    print("Stack is empty.")

