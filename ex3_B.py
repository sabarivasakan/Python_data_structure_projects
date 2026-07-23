class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
        
class Stack:
    def __init__(self):
        self.peek=None
    def push(self,data):
        new_node=Node(data)
        new_node.next=self.peek
        self.peek=new_node
    def pop(self):
        if self.peek is None:
            print("Under Flow")
            return
        print(f"The value {self.peek.data} is removed")
        t=self.peek.next
        
        self.peek=t
    def display(self):
        c=self.peek
        while c:
            print(c.data,end="->")
            c=c.next
        
if __name__=="__main__":
    i=0
    obj=Stack()
    ma=int(input("Enter the Max Value :"))
    while True:
        x=input("Enter leave space to end push : ")
        if x=='':
            break
        i+=1
        if i>ma:
            print("Stack is OverFlow")
            break
        else:
            obj.push(int(x))
    
    
    print("\nPeek : ",end="")
    obj.display()
    print()
    obj.pop()
    obj.pop()
    print("\nPeek : ",end="")
    obj.display()

        
