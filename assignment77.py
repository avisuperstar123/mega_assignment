# Write a Python program to calculate the simple interest. Formula to calculate simple interest is SI = (PRT)/100
p=float(input('enter the principle amount:'))
t=float(input('enter the time in years :'))
r=float(input('enter the rate of interest:'))
SI=(p*t*r)/100
print("the SI of the aount is:",SI)
