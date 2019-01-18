def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y
print("Select One Please:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. divide")

choice = input("Please Select One Now:")

num1 = int(input("Enter The First Number"))
num2 = int(input("Enter Your Second Number"))

if choice == '1':
    print(num1,"+",num2,"=",add(num1,num2))

elif choice == '2':
    print(num1,"-",num2,'=',add(num1,num2))

elif choice == '3':
    print(num1,'*',num2,'=',add(num1,num2))

elif choice == '4':
    print(num1,'/',num2,'=',divide(num1,num2))
else:
    print("Invalid Input")
