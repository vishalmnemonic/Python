Python from Michigan

Write a program that uses a print statement to say 'hello world'

# the code below almost works
print("hello world")

2.2 Write a program that uses input to prompt a user for their name and then welcomes them. Note that input will pop up a dialog box. Enter Sarah in the pop-up box when you are prompted so your output will match the desired output.

# The code below almost works

name = input("Enter your name")
print("Hello " + name)

2.3 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Use 35 hours and a rate of 2.75 per hour to test the program (the pay should be 96.25). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking or bad user data.

# This first line is provided for you

hrs = input("Enter Hours:")
rate_hr = input("Enter rate per hour:")
gross_pay = float(hrs)*float(rate_hr)
print("Pay: " + str(gross_pay))


3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input - assume the user types numbers properly.

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rate:")
r = float(rate)

if h <= 40.0 :
    pay = h*r
    print(pay)
else :
    pay = 40*r
    pay2 = (h-40)*r*1.5
    fpay=pay + pay2
    print(fpay)

3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.

score = input("Enter Score: ")
score = float(score)

if score >= 0.9 :
    print("A")
elif score >= 0.8 :
    print("B")
elif score >= 0.7 :
    print("C")
elif score >= 0.6 :
    print("D")
elif score < 0.6 :
    print("F")
else :
    print("error")
	
4.6 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours. Put the logic to do the computation of time-and-a-half in a function called computepay() and use the function to do the computation. The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly. Do not name your variable sum or use the sum() function.

def computepay(h,r):
    if h <= 40.0 :
        pay = h*r
        return(pay)
    else:
		pay = 40*r
		pay2 = (h-40)*r*1.5
		p = pay + pay2
		return p
    
hrs = input("Enter Hours:")
hrs = float(hrs)
rate = input("Enter rate:")
rate = float(rate)
p = computepay(hrs,rate)
print(p)

5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.


largest = None
smallest = None
while True:
	num = input("Enter a number: ")
	if num == "done" : break
	try :
		num = float(num)
	except :
		print("Invalid input")
		continue
	if largest == None :
		largest = num
	elif num > largest :
		largest = num
	if smallest == None :
		smallest = num
	elif num < smallest :
		smallest = num

print("Maximum is", int(largest))
print("Minimum is", int(smallest))

