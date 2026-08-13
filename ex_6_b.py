from collections import deque
m=input("Enter String : ")
t2=[i for i in m if i.isalpha()]
t1=deque(t2)
flag=True
while t1 and t2:
    if t1.popleft()==t2.pop():
        continue
    flag=False
    break
else:
    print(f"{m} is a pallindrome")
if not flag:
    print(f"Not a {m} pallindrome")
