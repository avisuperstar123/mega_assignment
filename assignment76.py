# Q76. Write a Python program to find the factorial of a given number
f=int(input('enter the number:'))
fact = 1;
a=f
if (f==0):
    print("the factorial of given number is",fact)
else:
    f=f-1
    while (f>0):
        a = a * f  
        f=f-1  
       
    print("the factorial of given number is",a)






    
