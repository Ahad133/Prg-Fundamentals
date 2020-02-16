a=eval(input("Enter Number: "))
if (a<0):
      print("Factorial of negative numbers doesn't exist")
elif (a==0):
    print("Factorial of zero is 1")
else:
    i=1
    f=1
    while (i<=a):
         f*=i
         i+=1
    print("Factorial of",a,"is",f)