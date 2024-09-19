"""
Collecting User Information
Author: Tania Bhan
"""
    
def collect_user_data(id_counter = 5000):
    name = input("Enter your name:")
    age =int(input("Enter your age:"))
    email = input("Enter your Email Address:")

    unique_id = id_counter + 1
    id_counter = unique_id


    print(f"\nUser Information:")
    print(f"Name:{name}")
    print(f"Age:{age}")
    print(f"Email Address:{email}")
    print(f"Unique ID:{unique_id}")

    return id_counter

id_counter = 5000
id_counter = collect_user_data(id_counter)




