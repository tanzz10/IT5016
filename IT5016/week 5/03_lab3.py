"""
Categorize and Recommendation based on Total Amount
Author: Tania Bhan
"""

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

total_amount = float(input("Enter your total amount:"))
categorize_request(total_amount)








    
    
        