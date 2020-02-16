s1=eval(input("Enter Marks in English = "))
s2=eval(input("Enter Marks in Urdu = "))
s3=eval(input("Enter Marks in Physics = "))
s4=eval(input("Enter Marks in Chemistry = "))
s5=eval(input("Enter Marks in Maths = "))
total=(s1+s2+s3+s4+s5)
per=((s1+s2+s3+s4+s5)/250)*100
print("Total marks =",total)
print("Percentage is =",round(per,2),"%")
if (per>=40 and per<=49):
    print("Grade D")
elif(per>=50 and per<=59):
    print("Grade C")
elif(per>=60 and per<=69):
    print("Grade B")
elif(per>=70 and per<=79):
    print("Grade A")
elif(per>=80 and per<=100):
    print("Grade A1")
else:fail
