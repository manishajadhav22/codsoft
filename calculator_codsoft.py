num1=int(input("Enter a first number  :"))
num2=int(input("Enter a second number :"))


while(True):
    print("Please Enter a choice :"+
        "1 -> Addition\n" +
        "2 -> Subtraction\n" +
        "3 -> Multiplication\n" +
        "4 -> Division\n")
    choice = int(input("enter a choice :"))

    if choice==1:
        addition=num1+num2
        print("Addtion ",+addition)
        
    elif choice==2:
        sub=num1-num2
        print("substraction ",+sub)
        
    elif choice==3:
        mul=num1*num2
        print("multiplication ",+mul)
        
    elif choice==4:
        div=num1/num2
        print("Division ",+div)
        
    else:
        print("please enter valid choice :")
        break
    

