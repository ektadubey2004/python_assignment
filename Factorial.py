#Write a program to calculate the factorial of an integer using recursion.
def fact(n):
   if n == 1:
       return n
   else:
       return n*fact(n-1)
num=int(input("Enter a number: "))
if num < 0:
   print("factorial does not exist")
elif num == 0:
   print("The factorial is 1")
else:
   print("The factorial of is", fact(num))