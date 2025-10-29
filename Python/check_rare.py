n,x=map(int,input().split())
while n>0 and x>0:
    if n%x==0:
        print("True")
    else:
        print("False")
    break
