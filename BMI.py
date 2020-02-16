w=eval(input("Enter weight in pounds: "))
h=eval(input("Enter height in inches: "))
bmi=(w*703)/h**2
if (bmi<18.5):
    print("Underweight")
elif (bmi>=18.5 and bmi<=24.9):
    print("Normal")
elif (bmi>=25.0 and bmi<=29.9):
    print("Overwieght")
else:
    print("Obese")