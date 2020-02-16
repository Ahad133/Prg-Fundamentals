a=int(input("Enter Age: "))
if(a<2):
    print("Person is a Baby")
elif(a>=2 and a<4):
    print("Person is a Toddler")
elif(a>=4 and a<13):
    print("Person is a Kid")
elif(a>=13 and a<20):
    print("Person is a Teenager")
elif(a>=20 and a<65):
    print("Person is an Adult")
elif(a>=65):
    print("Person is an Elder")