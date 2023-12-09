a=int(input("Enter the first number : "))
b=int(input("Enter the second number : "))
opera=input("Enter the operator : ")

if opera=='+':
    print("Sum of given two no is : a+b=",a+b)
elif opera=='-':
    print("Subtraction of given two no is : a-b=",a-b)
elif opera=='*':
    print("Multiplication of given two no is : a*b=",a*b)
elif opera=='/':
    print("Division of given two no is  : a/b=",a/b)
else:
    print("Enter the correct operator")

