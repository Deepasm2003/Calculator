#Name   : Deepa S M
#Email  : dpee271@gmail.com

#Code Start

def start_fun():
    print("\t\t\t CALCULATOR")
    print()
    print("1: Addition\t\t\t\t2: Substraction")
    print("3: Multiplication\t\t4:Division")
    print("5: Exit")
    print()

    choice = int(input('Select any one option from above: '))

    if choice==1:
        N1 = int(input('Enter First number: '))
        N2 = int(input('Enter Second number: '))
        N3=N1+N2
        print(N1,"+",N2,"=",N3)
        start_fun()

    elif choice==2:
        N1 = int(input('Enter First number: '))
        N2 = int(input('Enter Second number: '))
        N3=N1-N2
        print(N1,"-",N2,"=",N3)
        start_fun()

    elif choice==3:
        N1 = int(input('Enter First number: '))
        N2 = int(input('Enter Second number: '))
        N3=N1*N2
        print(N1,"*",N2,"=",N3)
        start_fun()

    elif choice==4:
        N1 = int(input('Enter First number: '))
        N2 = int(input('Enter Second number: '))
        N3=N1/N2
        print(N1,"/",N2,"=",N3)
        start_fun()

    elif choice==5:
        print("\t\tCalculator closed.")
        print("\t\tThank You")

    else:
        print("Select Correct option.")
        start_fun()

start_fun()

#Code End
