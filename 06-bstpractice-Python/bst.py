class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
 
class BST(object):
    def __init__(self, root):
        self.root = Node(root)
 
    def insert(self, new_val):
        newNode = Node(new_val)
        if(self.root == None):
            self.root = newNode
        else:
            current = self.root
            parent = self.root
            while(current != None):
                parent = current
                if(new_val < current.value):
                    current = current.left
                else:
                    current = current.right
            if(new_val < parent.value):
                parent.left = newNode
            else:
                parent.right = newNode
 
    def printSelf(self):
        print(self.root)
        
    def search(self, find_val):
        while self.root != None:
            if self.root.value == find_val:
                return True
            if self.root.value < find_val:
                self.root = self.root.right
            else:
                self.root = self.root.left
        return False

