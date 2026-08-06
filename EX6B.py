from collections import deque

m=input("Enter the String : ")
t2=[i for i in m if i.isalpha()]
t1=deque(t2)
flag=True
while t1 and t2:
        q=t1.popleft()
        p=t2.pop()
        if q==p:
                continue
        flag=False
        break
else:
        print(f"{m} is a Pollindrome")

if not flag:
        print(f"{m} is Not a Pollindrome")
