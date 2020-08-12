print("Calculator\n")
val1=int(input("Enter first number: "))
val2=int(input("Enter first number: "))

print("Enter choice:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division\n")

choice=int(input("Enter choice: "))

if choice==1:
    c=float(val1)+float(val2)
    print("The sum of ",val1," and ",val2," is: ",c)

elif choice==2:
    def subtract(a, b):
        if a >= b:
             return a - b
        else:
            return -1
    print(subtract(val1,val2))


elif choice==3:
    def multiply(a,b):
        print("Number 1: ", a)
        print("Number 2:", b)
        print("After Multiplication: ", a*b)

    multiply(val1,val2)

elif choice==4:
    def Division(a,b):
        print("Answer",a/b)
    Division(val1,val2)


