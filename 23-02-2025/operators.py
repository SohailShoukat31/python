# Operators in Python
# Types of Operators 
# Arithmetic Operators 
a= 5
b = 2
print(a + b)
print(a - b)
print(a * b)
print(a / b)  # Float Value always
print( 5 % b) # remainder 
print( a ** b)
print(a // b)
# Relational Operators
a = 50
b = 20
print(a == b)
print(a !=  b)
print( a >= b )
print(a > b)
print( a <= b)
print( a < b )

# Assignmet Operators 
num = 10
num = num + 10
print(num)

a = 10;
a += 10
print(a)


# Logical Operators

# Or not and 

val1 = 50
val2 = 50
print(val1 and val2)



def cal():
    num1 = float(input("Enter the first number: "))
    operator = input("Enter the operator: ")
    num2 = float(input("Enter the second value: "))

    if operator == "+":
        print("Sum : " , num1 + num2)  
    elif operator == "-":
        print("Diff :" , num1 - num2)
    elif operator == "*":
        print("Multiplication : ", num1 * num2) 
    elif operator == ("/"):
        print("Divide : " ,num1 / num2 )   

 
cal()




num = int(input("Enter the number to check even or odd"))

if num % 2 == 0 :
    print(num , "Is Even")
else: 
    print(num, "Is odd ")
        

   








