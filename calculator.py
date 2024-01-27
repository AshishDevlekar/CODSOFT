a=int(input("Enter First number: "))
b=int(input("Enter Second number: "))

operator = input("Enter operator: ")

match operator:
    case"+":
        print("Sum is",a + b)
    case"-":
        print("Subtraction is",a-b)
    case"*":
        print("Multiplication is", a*b)
    case"/":
        print("Divison is",a/b)        

