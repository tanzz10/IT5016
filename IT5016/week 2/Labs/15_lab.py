"""
Print name between two rows of stars
Author: Tania
"""
# (name):str=(input("enter name:"))
# length_of_name = len(name)
# stars = "*" * len(name)


name = "Alan Turing"
extra = 3

name_length = len(name)
stars_length = name_length + extra * 2

print("*" * stars_length)
print (" " * extra + name + " " * extra)
print("*" * stars_length)