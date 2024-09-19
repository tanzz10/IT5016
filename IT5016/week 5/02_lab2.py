"""
Calculating Total Amount
Author: Tania Bhan
"""

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

def main():
    print("Enter Item Details (Type 'finish' to end):")
    total_amount = calculate_total_amount()
    if not total_amount:
        print("No Details Were Entered")
    else:
        print(f"\nTotal Amount: ${total_amount:.2f}")

main()
