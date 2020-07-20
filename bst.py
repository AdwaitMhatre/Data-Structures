class Node:
    def __init__(self,data):
        self.data = data
        self.left_child = None
        self.right_child = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self,x):
        new_node = Node(x)
        if self.root == None:
            self.root = new_node
        else:
            self._insert(self.root,new_node)

    def _insert(self,current,x):
        if x.data > current.data:
            if current.right_child == None:
                current.right_child = x
            else:
                self._insert(current.right_child,x)
        elif x.data < current.data:
            if current.left_child == None:
                current.left_child = x
            else:
                self._insert(current.left_child,x)

    def in_order(self):
        self._in_order(self.root)
        print("")

    def _in_order(self,current):
        if current:
            self._in_order(current.left_child)
            print(current.data,end=" ")
            self._in_order(current.right_child)

    def pre_order(self):
        self._pre_order(self.root)
        print("")

    def _pre_order(self,current):
        if current:
            print(current.data,end=" ")
            self._pre_order(current.left_child)
            self._pre_order(current.right_child)

    def post_order(self):
        self._post_order(self.root)
        print("")

    def _post_order(self,current):
        if current:
            self._post_order(current.left_child)
            self._post_order(current.right_child)
            print(current.data,end=" ")

    def find_val(self, key):
        return self._find_val(self.root, key)

    def _find_val(self, curr, key):
        if curr:
            if key == curr.data:
                return print(f"{key} found in tree")
            elif key < curr.data:
                return self._find_val(curr.left_child, key)
            else:
                return self._find_val(curr.right_child, key)
        return print(f"{key} not found in tree")

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

tree = BST()
tree.insert("F")
tree.insert("C")
tree.insert("G")
tree.insert("A")
tree.insert("B")
tree.insert("K")
tree.insert("H")
tree.insert("E")
tree.insert("D")
tree.insert("I")
tree.insert("M")
tree.insert("J")
tree.insert("L")

tree.in_order()
tree.pre_order()
tree.post_order()
tree.find_val("Z")
tree.delete_val("C")
tree.in_order()
