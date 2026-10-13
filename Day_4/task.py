# # Revision 
# m = 0 != 0    
# n = 1 == 1    
# o = m and not n
# print(o)
# .................................................................

# p = 6 == 6   
# q = 5 != 5   
# # r = not p or q
# r = not (p or q)
# print(r)

# .................................................................

# p = 10 < 5   
# q = 3 == 3   
# r = 7 != 7   
# result = not (p or q and r)
# print(result)
# .......................................................
# Membership Operators
# in 
# not in 
# x="Sam"
# # print("Sa" in x)
# # print("aw" in x)
# print("aw" not in x)
# print("am" in x)
# ...................................................
# Conditional Statement 
# if
# if else
# if -elif else
# Nested if
# x=3
# print("Hello")
# if x==3:
#     print("Number is 3")
# print("Bye")

# To Check number is Even 
# x=int(input("Enter a Number: "))
# if x%2==1:
#     print("Odd")
# else:
#     print("Even")
# ............................
# To check number is positive negative or zero 

# x=0
# if x>0:
#     print("Positive")
# elif x<0:
#     print("Negative")
# else:
#     print("Zero")
# .............................................
# Nested if 

username="admin"
password=123445
if username=="admin":
    if password==1234:
        print("Welcome User")
    else:
        print("Password is incorrect")
else:
    print("Username is incorrect")
print("bye")