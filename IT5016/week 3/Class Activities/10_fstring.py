name = input("enter your name:")
age = input("enter your age:")

#fstrings
print(f"hello, {name},you are {age} years old.")


pi = 3.141592653589
formatted_pi = f"value of pi to 2 decimal places: {pi: .2f}"
print(formatted_pi)

salary = float(input("enter your weekly salary:"))
print(f"your weekly salary is: ${salary: .2f}")

#a = 15
#b = 10
#result = f"the result of {a} multiplied by {b} is {a*b}"
#print(result)

name = {"Tania"}
age = {"21"}
address = {"21 wordsworth road"}
info = f"""
name = {"Romil"}
age = {"21"}
address: {"Malolo Nadi"}
"""
print(info)
 



 # name = input("Enter your name")
# age = input("Enter your age")
# print("Hello,",name, ".You are", age," years old",sep="")
# # fstring
# print(f"Hello, {name}. you are {age} years old.")

# pi = 3.141592653589
# print(pi)
# formatted_pi = f"Value of pi to 2 decimal places: {pi: .2f}"
# print(formatted_pi)

# salary = float(input("Enter your weekly salary:"))
# print(f"Your weekly salary is ${salary: .2f}")

# a = 10
# b = 5
# result = f"The result of {a} multiplied by {b} is { a * b}"
# print(result)

name ="James"
age = 28
address ="121 Queen St"
info = f"""
Name: {name}
Age: {age}
Address:{address}
"""
print(info)
