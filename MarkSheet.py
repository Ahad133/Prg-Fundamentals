name=input("Enter Name: ")
fname=input("Enter Father's Name: ")
rollno=eval(input("Enter Roll Number: "))
course1=eval(input("Enter Marks in English: "))
course2=eval(input("Enter Marks in Urdu: "))
course3=eval(input("Enter Marks in Maths: "))
course4=eval(input("Enter Marks in Physics: "))
course5=eval(input("Enter Marks in Chemistry: "))
total_marks= course1+course2+course3+course4+course5
average=(total_marks)/5
percentage=round((total_marks*100)/250)
print()
print("\tMARKSHEET")
print("Name: ",name)
print("Father's Name: ",fname)
print("Roll Number: ",rollno)
print("Marks in English: ",course1)
print("Marks in Urdu: ",course2)
print("Marks in Maths: ",course3)
print("Marks in Physics: ",course4)
print("Marks in Chemistry: ",course5)
print("Total Marks: ",total_marks)
print("Average: ",average)
print("Percentage: ",percentage,"%")