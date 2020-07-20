class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self,x):
        '''add node to the end of the list'''
        new_node = Node(x)
        if self.head == None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next is not None:
                last_node = last_node.next
            last_node.next = new_node
            self.tail = new_node

    def remove(self):
        '''remove the last element of the queue'''
        current = self.head
        last = self.tail
        while current.next is not last:
            current = current.next
        current.next = None
        self.tail = current

    def length(self):
        '''return the length of the queue'''
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return print(f"The length of the queue is {count}")

    def is_empty(self):
        '''check if the queue is empty'''
        if not self.head:
            print("The queue is empty")
        else:
            print("The queue is not empty")

    def Display(self):
        '''display the queue'''
        to_print = ""
        current = self.head
        while current:
            to_print += str(current.data) + "->"
            current = current.next
        if to_print:
            if len(to_print) > 4:
                print("Head", " "*(len(to_print)-9),"Tail")
                print(" |", " "*(len(to_print)-6), "|")
                print(" V", " "*(len(to_print)-6), "V")
                return print("[" + to_print[:-2] + "]")
            else:
                print("Head & Tail")
                print(" |")
                print(" V")
                return print("[" + to_print[:-2] + "]")
        else:
            return print("[]")

my_queue = Queue()
my_queue.is_empty()
my_queue.add(9)
my_queue.Display()
my_queue.add(7)
my_queue.add(22)
my_queue.add("AB")
my_queue.Display()
my_queue.length()
my_queue.remove()
my_queue.Display()
my_queue.is_empty()
my_queue.Display()
