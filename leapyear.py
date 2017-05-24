y=input("enter year:")
if(y%400 == 0):
    print "%d is a leap year"%y
elif(y%100 == 0):
    print "%d is a not leap year"%y
elif(y%4 ==0):
    print "%d is a leap year"%y
else:
    print "%d is a not leap year"%y
