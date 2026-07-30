class Queue:
    def __init__(self):
        self.max=5
        self.front=-1
        self.rear=-1
        self.queue= []

    def enqueue(self,data):
        if self.rear==-1:
            self.queue.append(data)
            self.rear+=1
            self.front=0
        elif self.max>=self.rear:
            self.queue.append(data)
            self.rear+=1
        else:
            print("Queue is Full")
    def dequeue(self):
        if self.rear ==0:
            print("Queue is Empty")
            return
        else:
            print(f"{self.queue[self.front]} is Removed")
            self.front+=1
        if self.rear== self.front:
            self.rear=self.front=-1
    def display_all(self):
        st=self.front
        ed=self.rear
        
        for i in range(st,ed+1):
            print(f"{self.queue[i]}-->",end="")
            
        print(None)
    def show(self):
        print(self.queue)
obj = Queue()
tree=True

while True:
    
    x=input("Enter the data to add in queue : ")
    if x=='':
        break
    else:
        obj.enqueue(int(x))
obj.display_all()
obj.dequeue()
obj.dequeue()
obj.dequeue()
obj.display_all()
            
