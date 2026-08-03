a = int(input("enter the value of a:"))
if a <= 1:
    print (a,"is not a prime number")
for i in range (2, a):
    if a % i  == 0:
        print (a, "is not a prime number")
        break
else:
    print (a, "is a prime number")