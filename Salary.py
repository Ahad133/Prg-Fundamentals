a=int(input("Enter Years of Service: "))
b=input("Enter Qualification: ")
if(a >= 10 and b == "Masters"):
    print("Salary: 150,000")
elif(a >= 10 and b == "Bachelors"):
    print("Salary: 100,000")
elif(a < 10 and b == "Masters"):
    print("Salary: 100,000")
elif(a < 10 and b == "Bachelors"):
    print("Salary: 70,000")
