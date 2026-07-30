operator =["+","-","*","/","(",")","^"]
prior={
    "+":1,
    "-":1,
    "*":2,
    "/":2,
    "^":3,
    }
def itp(exp):
    out=""
    stack=[]
    print(f"out : {out} \n stack : {stack}")
    for ch in exp:
        if ch not in operator:
            out+=ch
        elif ch == "(":
            stack.append(ch)
        elif ch ==")":
            while stack and stack[-1]!="(":
                out+=stack.pop()
            stack.pop()
        else:
            while stack and stack[-1]!="(" and prior[ch] <= prior[stack[-1]]:
                out+= stack.pop()
            stack.append(ch)
       
    while stack:
        out+=stack.pop()
    print("The output is : ",out)
    return out

if __name__ =="__main__":
    m=input("Enter the infix Expression : ")
    print("Output Post Fix Expression : ", itp(m))
    
