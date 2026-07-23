class Stack:
    def __init__(self):
        self.top=[]
    def push(self,value):
        self.top.append(value)
    def is_empty(self):
        return self.top==[]
    def pop(self):
        if self.is_empty():
            print("Stack is Under Flow")
            return
        print(f"The value {self.top[-1]} is removed")
        self.top.pop()
    def peek(self):
        return self.top[-1]
    def disp(self):
        print(len(self.top[::-1]))
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
    
    
    print("\nPeek ",obj.peek())
    obj.pop()
    obj.pop()
    print("\nPeek ",obj.peek())
    obj.pop()
    obj.pop()
    obj.pop()
        


        
        
