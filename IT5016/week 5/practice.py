def collect_user_data(id_counter=5000):
    name = input("Enter your name:")
    age = int(input("Enter your age:"))
    email = input("Enter your email:")

    unique_id = id_counter + 1
    id_counter = unique_id

    print(f"\nUser Information:")
    print(f"Name:{name}")
    print(f"Age:{age}")
    print(f"Email Address:{email}")
    print(f"Unique ID:{unique_id}")

    return unique_id,name,age,email,id_counter

def calculate_total_amount():

    total_amount = 0
    while True:
        price_of_item = input("Enter Item Name and Price (e.g., Cable $200):")
        if price_of_item.lower() == 'finish':
            break
        try:
            Item_Name, Price = price_of_item.rsplit(maxsplit=1)
            Item_Name = str(Item_Name)
            Price = Price.replace("$","")
            Price = float(Price)
            total_amount += Price
        except ValueError:
            print("Invalid Input. Please follow the format.")
    return total_amount

def categorize_request(total_amount):
    if total_amount < 150:
       Category = "Low"
       Recommendation = "Proceed with standard processing."
    else:
        Category = "High"
        Recommendation = "Review for potential discounts. "
    
    print("\nRequest Summary:")
    print(f"Total Amount:${total_amount:.2f}")
    print(f"Category:{Category}")
    print(f"Recommendation:{Recommendation}")

    return Category, Recommendation

def create_detailed_report(unique_id,name,age,email,total_amount,Category,Recommendation):
    print(f"\nDetailed Report:")
    print(f"Name:{name}")
    print(f"Age:{age}")
    print(f"Email Address:{email}")
    print(f"Unique ID:{unique_id}")
    print(f"Total Amount:{total_amount}")
    print(f"Category:{Category}")
    print(f"Recommendation:{Recommendation}")

def main():
    id_counter = 5000
    unique_id, name, age, email, id_counter = collect_user_data(id_counter=5000)
    print("\nEnter Item Details (Type 'finish' to end):")
    total_amount = calculate_total_amount()
    Category, Recommendation = categorize_request(total_amount)
    create_detailed_report(unique_id, name, age, email, total_amount, Category, Recommendation)
main()
    #practice
    



