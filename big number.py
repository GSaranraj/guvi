a=input("Enter the first number:")
b=input("Enter the second number:")
c=input("Enter the third number:")
if(b<=a and c<=a):
    print "%d is a biggest number"%a
elif(c<=b and a<=b ):
    print "%d is a biggest number"%b
else:
    print "%d is a biggest number"%c
