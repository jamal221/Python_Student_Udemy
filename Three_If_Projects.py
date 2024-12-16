#Three projects for If statments
def design_Traingle():
    try:
        a=int(input("Insert the first edge please: "))
        b=int(input("Insert the Second edge please: "))
        c=int(input("Insert the Theird edge please: "))
        flag=0
        if a<(b+c):
            flag+=1
        if b<(a+c):
            flag+=1
        if c<(a+b):
            flag+=1
        if flag==3:
            print("You can Designe Triangle easily")
        else:
            print("You could not designe your triangle at the moment")
    except:
        print("Please insert number")
# check max between three number
def max2Digits():
    try:
        a=int(input("Insert the first number please: "))
        b=int(input("Insert the Second number please: "))
        c=int(input("Insert the Theird number please: "))
        max=a
        if a<=b<=c:
            max=c
        if a<=c<=b:
            max=b
        if b<=a<=c:
            max=c
        if b<=c<=a:
            max=a
        if c<=a<=b:
            max=b
        if c<=b<=a:
            max=a
        print(max)
    except:
        print("Please insert number")
#Check Username and password username=Admin and password=123456
def userPass():
    try:
        a=(input("Insert the Username please: "))
        b=(input("Insert the password please: "))
        if a=="Admin" and b=="123456":
            print("Welcome")
        else:
            print("Please notice to your input")
    except:
        print("Please insert number")        
