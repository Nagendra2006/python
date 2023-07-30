def Palindrome(original):
    reverseNum = 0
    temp = original

    while (temp > 0):
        lastDigit = temp % 10
        reverseNum = reverseNum * 10 + lastDigit
        temp = temp / 10

    if (original == reverseNum):
        print("it is a palindrome number")
    else:
    	return 0
a=input("enter the integer number:")
b=Palindrome(a)
print(b)        
        
