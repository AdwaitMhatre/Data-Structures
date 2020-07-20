class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append_val(self,x):
        '''add to the end of the list'''
        new_node = Node(x)

        if self.head == None:
            self.head = new_node
            return print(f"appending {new_node.data} to the list...")
        else:
            print(f"appending {new_node.data} to the list...")
            last_node = self.head
            while last_node.next is not None:
                last_node = last_node.next
            last_node.next = new_node

    def prepend_val(self,x):
        '''add to the start of the list'''
        new_node = Node(x)
        print(f"prepending {new_node.data} to the list...")
        new_node.next = self.head
        self.head = new_node

    def insert_after(self,previous_node,data):
        if not previous_node:
            print("Given previous node doesnt exist in the list")

        new_node = Node(previous_node)
        new_node.next = previous_node.next
        previous_node.next = new_node

    def delete_by_index(self,x):
        '''delete element acc to user ip index'''
        print(f"removing element at index {x}...")
        count = 0
        current = self.head
        previous = None
        while current:
            if count == x:
                if previous:
                    previous.next = current.next
                    current.next = None
                    return
                else:
                    current.next = None
                    return
            count += 1
            previous = current
            current = current.next
        return print("The given index is invalid")

    def Display(self):
        to_print = ""
        print("Head")
        print(" |")
        print(" V")
        current = self.head
        while current is not None:
            # print(element.data)
            to_print += str(current.data) + "->"
            current = current.next
        if to_print:
            return print("[" + to_print[:-2] + "]")
        else:
            return print("[]")

    def search_val(self, x):
        '''return indices where x was found'''
        element = x
        count = 0
        current = self.head
        while current:
            if current.data == element:
                return print(f"The element {element} was found at index {count} ")
            count += 1
            current = current.next
    def length(self):
        '''return the length of the list, rep'd by number of nodes'''
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return print(f"The length of the list is {count}")

def reverse_list_iter(self):
    '''reverse the list using iterative'''
    print("reversing the list...")
    current = self.head
    previous = None
    while current:
        next = current.next
        current.next = previous
        previous = current
        current = next
    self.head = previous

def reverse_list_recur(self):
    '''reverse the list using recusrion'''
    print("reversing the list...")
    def recur(current,previous):
        if current == None:
            return previous
        next = current.next
        current.next = previous
        previous = current
        current = next
        return recur(current,previous)
    self.head = recur(current=self.head,previous=None)

list = LinkedList()
list.append_val(32)
list.append_val(11)
list.append_val(7)
list.prepend_val("G")
list.prepend_val(69)
list.append_val("A")
list.prepend_val(88)
list.Display()
list.length()
list.search_val("A")
list.delete_by_index(3)
list.Display()
list.reverse_list_iter()
list.Display()
list.reverse_list_recur()
list.Display()
