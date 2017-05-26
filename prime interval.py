numb = int(input("Enter a number: "))
if numb > 1:
   # check for factors
   for i in range(2,numb):
       if (numb % i) == 0:
           print(numb,"is not a prime number")
           print(i,"times",numb//i,"is",numb)
           break
   else:
       print(numb,"is a prime number") 
else:
   print(numb,"is not a prime number")
