# String  or Text 
# ''  |  ""   
name = "Sohail"
greetings = 'How are you'

print(name , greetings)

# Number
# Float 
num1 = 99.9
num2 = 0.5
print(num1 , num2)

# Integer
x = 10
y = 20
print(x)
print(type(x))

# Boolean 
is_raining = True
is_sunny = False
print(is_raining, is_sunny)

# Lists
fruits = ["Apple" , "Banana" , "Carrot"]
numbers = [1 , 2 , 3 , 4 , 5]
print(fruits)
print(numbers)


# Tuples 

# Tuples is data type like list but we can not change real example of life 

days = ("Monday" , "Tuesday" , "Wednesday")
print(days)

# List is a mutable we can change value 
# Tuples is a immutable we can not change value 

#  Dictionary  Data Type 

# Which store data in  Key-Value pairs

student = {
    "name" : "sohail",
    "age" : 20,
    "grade" : "A"

}
print(student)

# None 
a = None
print(a)


# Complex 
mix = 1j
print(mix)


# Range 

x = range(10);
print(x)
y = range(5 , 10)
print(y)

# Project
student = {
    "name" : "Ahmed",
    "age"  : 22,
    "subjects" : ["Math" , "Science" , "English"]
}

print("Student Name:", student["name"])
print("Student Age :" , student["age"])
print("Student Subjects : " , student["subjects"])