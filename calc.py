print("simple calculater")
print("1.addition")
print("2.substraction")
print("3.multiplication")
print("4.division")

choice = int (input("enter the choice 1/2/3/4 : "))

num1 = float(input("enter first number :"))
num2 = float(input("enter second number :"))

if choice == 1 :
    print("result : num1+num2")
elif choice == 2 :
    print("result : num1-num2")    
elif choice == 3 :
    print("result : num1*num2")
elif choice == 4 :
    if num2!=0 :
        print("result : num1/num2")    
    else:
        print("division by zero is not allowed")    
else:
    print("invalid choice")            