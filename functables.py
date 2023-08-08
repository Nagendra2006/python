def fact(n):
    if(n==1):
        return 1
    else:
        return n*fact(n-1)
a=int(input("enter the integer:"))
b=fact(a)
print("the fact is :",b)
#multiplication table
def multi():
    b=1
    while(b<=5):
        l=1
        while(l<=10):
            print(l,"*",b,"=",(l*b))
            l=l+1
        b=b+1
    print("\n")
multi()   