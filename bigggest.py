#given number is even or odd
h=int(input("enter an integer"))
if(h%2==0):
    print("it is even")
else:
    print("it is odd")
#finding biggest of three numbers
a,b,c=[int(n) for n in input("enter the a,b,c values:").split(',')]
big=b if b>a else a
big=c if c>big else big
print("the biggest is:",big)