class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
    def enqueue(self,data):
        new=Node(data)
        if self.rear is None:
            self.front=self.rear=new
            return
        self.rear.next=new
        self.rear=new
    def dequeue(self):
        if self.front is None:
            return
        data = self.front.data
        print("The ", data ," is Removed")
        self.front=self.front.next
        if self.front is None:
            self.rear=None
        return data
    def display(self):
            if self.front is None:
                return None
            return self.front.data
    def display_all(self):
        if self.front is None:
            return None
        temp= self.front
        print("The value in Queue : ")
        while temp:
            print(f"{temp.data}-->",end="")
            temp=temp.next
        print(None)
obj = Queue()
while True:
        x=input("Enter leave space to end push : ")
        if x=='':
            break
        else:
            obj.enqueue(int(x))
obj.display_all()
obj.dequeue()
obj.dequeue()
obj.display_all()

