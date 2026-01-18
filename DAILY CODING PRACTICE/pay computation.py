# WAP FOR pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
# PAY program SHOULD BE using try and except so that your program,
# handles non-numeric input gracefully by printing a message and exiting the program.

try:
 hr = float(input('ENTER HOUR WORKED:'))
 rate= float(input('ENTER RATE :')) 
except:
 print("error, please enter numeric value:")
 quit()
     
if (hr<=40):
    pay = hr*rate
else:
    extra_hr = (hr-40) 
    pay=(40*rate + extra_hr*rate*1.5)
    
print("PAY:",pay)        

    


  

