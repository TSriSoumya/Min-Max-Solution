def calmin(lis):
    l=len(lis)
    i=0
    lk=[]
    while i<l-1:
        s=min(lis[i],lis[i+1])
        lk.append(s)
        i+=2
    if len(lk)==1:
        print(lk[0])
        pass
    else:
        calmax(lk)
    pass

def calmax(lis):
    l=len(lis)
    i=0
    lk=[]
    while i<l-1:
        s=max(lis[i],lis[i+1])
        lk.append(s)
        i+=2
    if len(lk)==1:
        print(lk[0])
        pass
    else:
        calmin(lk)
    pass

lis=[]
d=int(input("Enter the depth of the complete binary tree: "))
print("Enter",pow(2,d),"nodes values: ")
lis = [int(x) for x in input().split()]
l=len(lis)
if l!=pow(2,d):
    print("Entered incorrect no: of node values.")
    pass
a=input("Enter 'min' or 'max': ")
if a=='max':
    if d%2==0:
        print("Optimal solution ",end="")
        calmin(lis)
    else:
        print("Optimal solution ",end="")
        calmax(lis)
elif a=='min':
    if d%2==0:
        print("Min solution ",end="")
        calmax(lis)
    else:
        print("Min solution ",end="")
        calmin(lis)
pass
