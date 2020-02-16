for i in range(1,3+1):
    print("*****Login Page*****")
    u=input("User name: ")
    p=input("Password: ")
    userName=u.lower()
    password=p.lower()
    print("************")
    if (userName=='abdul.ahad133' and password=='python'):
        print("Homepage")
        print("*********")
        print("Menu")
        print("*********")
        print("Setting")
        print("*********")
        print("Contact us")
        print("*********")
    else:
        a=input("Re-enter the data? Y/N\n")
        y_n=a.upper()
        if (y_n=='Y'):
            continue
        else:
            break