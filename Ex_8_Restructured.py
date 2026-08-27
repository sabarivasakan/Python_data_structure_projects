#Binary Search Node
class Node:
    def __init__(self,data):
        self.left=None
        self.right= None
        self.data=data
#Binary Search Tree Operation
class Tree:
    def __init__(self):
        self.root=None
        
    def insert(self,data):
        self.root=self.add(self.root,data)
    def add(self,root,data):
        if root is None:
            return Node(data)
        #if data is greater and right is None
        if root.data<data and root.right is None:
            root.right=Node(data)
        #if data is smaller and left is None
        elif root.data>data and root.left is None:
            root.left=Node(data)
        #if data is greater and ther is a child on right
        elif root.data<data:
            self.add(root.right,data)
        #if data is smaller and ther is a child on left
        else:
            self.add(root.left,data)
        return root
    #Search Value
    def search(self,data):
        root=self.root
        return self.search_child(root,data)
    def search_child(self,root,data):
        #if reach an end
        if root is None:
            print(f"\n{data} is not present in the Tree")
            return False
        # both are equal
        if root.data==data:
            print(f"\n{data} is present in the Tree")
        #data is Lower
        elif root.data>data:
            self.search_child(root.left,data)
        #data is Greater
        else:
            self.search_child(root.right,data)
    #delete
    def delete(self, data):
        self.root = self.delete_node(self.root, data)
        print(f"the {data} is Removed")

    def delete_node(self, root, data):
        if root is None:
            return root
        if data < root.data:
            root.left = self.delete_node(root.left, data)
        elif data > root.data:
            root.right = self.delete_node(root.right, data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            min_node = self.find_min(root.right)
            root.data = min_node.data
            root.right = self.delete_node(root.right, min_node.data)

        return root
    def inorder(self):
        root=self.root
        self.init(root)
    def init(self,root):
        if root:
            self.init(root.left)
            print(root.data,end=" , ")
            self.init(root.right)
    def postorder(self):
        root=self.root
        self.poin(root)
    def poin(self,root):
        if not root:
            return
        self.poin(root.left)
        self.poin(root.right)
        print(root.data,end=" , ")
    def preorder(self):
        root=self.root
        self.prein(root)
    def prein(self,root):
        if not root:
            return None
        print(root.data,end=" , ")
        self.prein(root.left)
        self.prein(root.right)
    
obj=Tree()
print("start")

while True:
    x=input("Enter the Book Log entry Time : ")
    if not x:
        break
    obj.insert(float(x))
obj.inorder()
obj.search(3.5)
obj.delete(3.5)
print("Inorder : [",end="")
obj.inorder()
print(" None ]")
print("\nPreOrder : [",end="")

obj.preorder()
print(" None ]")
print("\nPostOrder : [",end="")
obj.postorder()
print(" None ]")


