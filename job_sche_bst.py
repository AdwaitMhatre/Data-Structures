from datetime import datetime,timedelta

class Node:
    def __init__(self,key):
        sch_time,duration,name_of_job = key.split(",")
        raw_time = datetime.strptime(sch_time,"%H:%M")
        key = raw_time.time()
        end_time = (raw_time + timedelta(minutes=int(duration))).time()
        self.data = key
        self.duration = duration
        self.sch_end_time = end_time
        self.name_of_job = name_of_job.rstrip()
        self.left_child = None
        self.right_child = None

    def __str__(self):
        return f"Time: {self.data}, Duration: {self.duration} min, Job Name: {self.name_of_job}"

class BST:
    def __init__(self):
        self.root=None

    def insert(self,key):
        if not isinstance(key, Node):
            new_node = Node(key)
        if self.root == None:
            self.root = new_node
            self.help_print(new_node,True)
        else:
            self._insert(self.root,new_node)

    def _insert(self,curr,key):
        if key.data < curr.data and key.sch_end_time <= curr.data:
            if curr.left_child == None:
                curr.left_child = key
                self.help_print(key,True)
            else:
                self._insert(curr.left_child,key)
        elif key.data > curr.data and key.data >= curr.sch_end_time:
            if curr.right_child == None:
                curr.right_child = key
                self.help_print(key,True)
            else:
                self._insert(curr.right_child,key)
        else:
            self.help_print(key,False)

    def help_print(self,key,succeeded):
        if succeeded:
            print(f"Added:\t\t {key.name_of_job}")
            print(f"Begin:\t\t {key.data}")
            print(f"End:\t\t {key.sch_end_time}")
            print("-"*60)
        else:
            print(f"Rejected:\t {key.name_of_job}")
            print(f"Begin:\t\t {key.data}")
            print(f"End:\t\t {key.sch_end_time}")
            print("Reason:\t Time slot overlap, please verify")
            print("-"*60)

    def length(self):
        return self._length(self.root)

    def _length(self,curr):
        if not curr:
            return 0
        return 1 + self._length(curr.left_child) + self._length(curr.right_child)

    def find_val(self,key):
        return self._find_val(self.root,key)

    def _find_val(self,curr,key):
        if curr:
            if key == curr.data:
                return curr
            elif key < curr.data:
                return self._find_val(curr.left_child,key)
            elif key > curr.data:
                return self._find_val(curr.right_child,key)
        else:
            return print("Given info not found")

    def in_order(self):
        print("Full job schedule for today:")
        print("-"*60)
        self._in_order(self.root)
        print("-"*60)

    def _in_order(self,current):
        if current:
            self._in_order(current.left_child)
            print(current)
            self._in_order(current.right_child)

    def min_right_child(self,curr):
        if curr.left_child == None:
            return curr
        else:
            return self.min_right_child(curr.left_child)

    def delete_val(self,key):
        self._delete_val(self.root,None,None,key)

    def _delete_val(self,curr,prev,is_left,key):
        if curr:
            if key == curr.data:
                if curr.right_child and curr.left_child:
                    min_value = self.min_right_child(curr.right_child)
                    curr.data = min_value.data
                    self._delete_val(curr.right_child,curr,False,curr.data)
                if curr.right_child == None and curr.left_child == None:
                    if prev:
                        if is_left:
                            prev.left_child = None
                        else:
                            prev.right_child = None
                    else:
                        self.root = None
                elif curr.left_child == None:
                    if prev:
                        if is_left:
                            prev.left_child = curr.right_child
                        else:
                            prev.right_child = curr.right_child
                    else:
                        self.root = curr.right_child
                elif curr.right_child == None:
                    if prev:
                        if is_left:
                            prev.left_child = curr.left_child
                        else:
                            prev.right_child = curr.left_child
                    else:
                        self.root = curr.left_child
            elif key < curr.data:
                self._delete_val(curr.left_child,curr,True,key)
            elif key > curr.data:
                self._delete_val(curr.right_child,curr,False,key)

        else:
            print(f"{key} not found")
