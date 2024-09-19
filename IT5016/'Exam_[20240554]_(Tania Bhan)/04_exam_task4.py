"""
Display of Staff's Basic Information and Total Requisition
Author: Tania Tanisha Bhan
"""

def staff_info(unique_id=10000):
    date = input("Enter today's date:")
    staff_id = input("Enter your Staff ID:")
    staff_name = input("Enter your name:")

    requisition_id = unique_id + 1
    unique_id = requisition_id

    print(f"\nPrinting Staff Information:")
    print(f"Date:{date}")
    print(f"Staff ID:{staff_id}")
    print(f"Staff Name:{staff_name}")
    print(f"Requisition ID:{requisition_id}")

    return date,requisition_id,staff_id,staff_name,unique_id

# unique_id = 10000
# staff_info = staff_info(unique_id)

def requisition_total():
    total_value = 0
    while True:
        price_of_item = input("Enter each item name with a price (e.g., Tea $20):")
        if price_of_item.lower() == 'finish':
            break
        try:
            item_name, price = price_of_item.rsplit(maxsplit=1)
            item_name = str(item_name)
            price = price.replace("$","")
            price = float(price)
            total_value += price
        except ValueError:
            print("Invalid Input. Please follow the format(e.g., Tea $20):")
    return total_value

# def main():
#     print(f"\nRequisition Items (type 'finish' to end):")
#     total_value = requisition_total()
#     if not total_value:
#         print("Invalid")
#     else:
#         print(f"Requisition Total:\n${total_value:.2f}")
# main()

def requisition_approval(total_value,staff_id,requisition_id):

    if total_value < 500:
       Status = "Approved"
       Reference_Number = staff_id,requisition_id        #ref_num = str(staffid) + id_tsr[-3:]
    else:
        Status = "Pending"

    print(f"Requisition Approval:")
    print(f"Total:${total_value:.2f}")
    print(f"Status:{Status}")
    print(f"Approval Reference Number:{Reference_Number}")
    
    return Status, Reference_Number

# staff_id = input(f"Enter Staff ID:")
# requisition_id = input(f"Enter Requisition ID:")
# total_value = float(input("Enter Total:"))
# requisition_approval(total_value,staff_id,requisition_id)


def display_requisitions(date,requisition_id,staff_id,staff_name,total_value,Status,Reference_Number):

    print(f"\nPrinting Requisitions:")
    print(f"Date:{date}")
    print(f"Requisition ID:{requisition_id}")
    print(f"Staff ID:{staff_id}")
    print(f"Staff Name:{staff_name}")
    print(f"Total:${total_value:.2f}")
    print(f"Status:{Status}")
    print(f"Approval Reference Number:{Reference_Number}")

def main():
    unique_id = 10000
    date,requisition_id,staff_id,staff_name,unique_id = staff_info(unique_id)
    print(f"\nRequisition Items (type 'finish' to end):")
    total_value = requisition_total()
    Status,Reference_Number = requisition_approval(total_value,staff_id,requisition_id)
    display_requisitions(date,requisition_id,staff_id,staff_name,total_value,Status,Reference_Number)

main()