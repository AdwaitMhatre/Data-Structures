class Node:
    def __init__(self,data):
        '''initialize the node'''
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        '''initialize the stack'''
        self.stack_pointer = None

    def push(self,x):
        '''add a value to top of stack'''
        new_node = Node(x)
        if self.stack_pointer == None:
            print(f"adding {new_node.data} to the stack...")
            self.stack_pointer = new_node
        else:
            print(f"adding {new_node.data} to the stack...")
            new_node.next = self.stack_pointer
            self.stack_pointer = new_node

    def pop(self):
        '''remove the topmost value of stack'''
        current = self.stack_pointer
        if self.stack_pointer == None:
            return print("stack is empty")
        else:
            self.stack_pointer = current.next
            current.next = None
            return print(f"removing {current.data} from the stack...")

    def Display(self):
       '''Display the stack'''
       to_print = ""
       print(" SP")
       print(" |")
       print(" V")
       current = self.stack_pointer
       while current is not None:
           to_print += str(current.data) + "->"
           current = current.next
       if to_print:
           return print("[" + to_print[:-2] + "]")
       else:
           return print("[]")

    def is_empty(self):
        '''check if the stack is empty'''
        if not self.stack_pointer:
            print("The stack is empty")
        else:
            print("The stack is not empty")

    def length(self):
        '''return the length of the stack'''
        count = 0
        current = self.stack_pointer
        while current:
            count += 1
            current = current.next
        return print(f"The length of the stack is {count}")

my_stack = Stack()
my_stack.is_empty()
my_stack.push(10)
my_stack.push(7)
my_stack.push(69)
my_stack.push(54)
my_stack.Display()
my_stack.pop()
my_stack.Display()
my_stack.is_empty()
my_stack.length()
