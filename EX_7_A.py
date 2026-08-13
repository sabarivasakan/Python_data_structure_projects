class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def create_tree():
    title=input("Enter title of Book : ")
    if title=="-1":
        return None
    root=Node(title)
    print("The value of left child is ", title)
    root.left=create_tree()
    print(f"The Value of Right child is {title}")
    root.right=create_tree()
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end=" -->")
        inorder(root.right)

def postorder(root):
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data,end=" --> ")
def preorder(root):
    if not root:
        return None
    print(root.data,end=" --> ")
    preorder(root.left)
    preorder(root.right)
root =create_tree()
print(f"Inorder :")
print(inorder(root))
print(f"PostOrder : " )
print(postorder(root))
print("PreOrder : " )
print(preorder(root))


            
    
        
    
