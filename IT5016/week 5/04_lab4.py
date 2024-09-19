"""
Detailed Report Based on User Data and Category
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

    return unique_id, name, age, email, id_counter

# id_counter = 5000
# id_counter = collect_user_data(id_counter)

def calculate_total_amount():
    price_of_item = []
    total_amount = 0
    while True:
        price_of_item = input("Item Name and Price (e.g., Cables $200):")
        if price_of_item.lower() == 'finish':
            break
        try:
             Item_Name, Price = price_of_item.rsplit(maxsplit=1)
             Item_Name = str(Item_Name)
             Price = Price.replace('$', '')
             Price = float(Price)
             total_amount += Price
        except ValueError:
             print("Invalid input. Please enter in the format 'Item Name and Price'.")
    return total_amount

# def main():
#     print("\nEnter Item Details (Type 'finish' to end):")
#     total_amount = calculate_total_amount()
#     if not total_amount:
#         print("No Details Were Entered")
#     else:
#         print(f"\nTotal Amount: ${total_amount:.2f}")

# main()

def categorize_request(total_amount):

    if total_amount < 150:
        Category = "Low"
        Recommendation = "Proceed with standard processing."
    else:
        Category = "High"
        Recommendation = "Review for potential discounts."

    
    print("\nRequest Summary:")
    print(f"Total Amount:${total_amount:.2f}")
    print(f"Category:{Category}")
    print(f"Recommendation:{Recommendation}")

    return Category, Recommendation

# total_amount = (input("\nEnter your total amount:"))
# total_amount = float(total_amount.replace('$', ''))

# categorize_request(total_amount)


def create_detailed_report(unique_id, name, age, email, total_amount, Category, Recommendation):
    
    print("\nDetailed Report:")
    print(f"Unique ID:{unique_id}")
    print(f"User Name:{name}")
    print(f"Age:{age}")
    print(f"Email:{email}")
    print(f"Total Amount:{total_amount:.2f}")
    print(f"Category:{Category}")
    print(f"Recommendation:{Recommendation}")

def main():
    # Start with the initial id_counter value
    id_counter = 5000

    # Collect user data
    unique_id, name, age, email, id_counter = collect_user_data(id_counter=5000)

    # Calculate total amount
    print("\nEnter Item Details (Type 'finish' to end):")
    total_amount = calculate_total_amount()

    # Categorize request based on total amount
    Category, Recommendation = categorize_request(total_amount)

    # Create a detailed report
    create_detailed_report(unique_id, name, age, email, total_amount, Category, Recommendation)

# Run the main function
main()

