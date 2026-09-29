# Variables (container to hold values)
x=23
x="Sam"
x=23.34
x=True

# Rules to define a variable 
# 1 It should start with letter or underscore (_)
age=12
_ageofperson=23
# 1age=22
# 2. It should contain letter , numbers or underscore
name_of_person="Sam"
# name@emp="Danny"
# name1="Joey"
# print(name_of_person, name1, name@emp)
# .................................................
# 3. Variable names are case sensitive 
age=12
Age=23
AGE=34
# 4. Do not use Keywords as variable name 
# class="B"
# class1="C"
# print(class)
# print(class1)
# .........................................................
# Data Types 
# x=True
# print(x, type(x))
# .........................................
# Implicit Type casting
# x=23
# print(x,type(x))
# x="Danny"
# print(x,type(x))
# ......................................
# Explicit Type Casting

# Input Taking 
# val=input("Enter a number :")
# print(val, type(val))
# val=int(val)
# print(val, type(val))

# x="2345"
# # y=int(x)
# y=float(x)
# print(y,type(y))
# z=bool(0.1)
# print(z,type(z))
# print(type(str(23)))
# ......................................
# Multiple values to multiple variable 
# a=12
# b=23
# c=34
# print(a,b,c)
# a,b,c=12,23,34
# print(a,b,c)

# One Value to multiple variables
# a=12
# b=12
# c=12
# print(a,b,c)

# a=b=c=12
# print(a,b,c)
# ....................................................
# Formatted String 

# name="Joey"
# course="BCA"
# Batch="B"
# RollNo=12

# print(f"My name is {name}.I am from {course} course, {Batch} batch. My roll number is {RollNo}")
# .............................................................................
# Mathematical Operators 
# a=5
# b=2
# print(a%b)
# print(a/b)
# print(a**b)

a=1
b=2
c=3
d=4
# sum=d*2+a*2+b*2+c*2    # 20
sum=(d+a+b+c)*2
print(sum)