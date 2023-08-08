#finding factorial of given number
n=int(input("Enter number: "))
fact=1
while(n>0):
    fact=fact*n
    n=n-1
print("Fact is ",fact)
#priinting the table up to 1 to 5

b=1
while(b<=5):
    a=1
    while(a<=10):
        print(a,"*",b,"=",(a*b))
        a=a+1
    b=b+1
    print("\n")
print("done")