#factorial
n=int(input ())
for y in range (0,n):
    num = int(input () )
    fact=1
    for i in range (2,num+1):
        fact = i*fact
    print (fact)
