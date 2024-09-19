"""
Requisition Approval Decisions Based On Conditions
Author: Tania Tanisha Bhan
"""
def requisition_approval(total_value,staff_id,requisition_id):

    if total_value < 500:
       Status = "Approved"
       Reference_Number = staff_id,requisition_id
    else:
        Status = "Pending"

    print(f"Requisition Approval:")
    print(f"Total:${total_value:.2f}")
    print(f"Status:{Status}")
    print(f"Approval Reference Number:{Reference_Number}")
    
    return Status, Reference_Number

staff_id = input(f"Enter Staff ID:")
requisition_id = input(f"Enter Requisition ID:")
total_value = float(input("Enter Total:"))
requisition_approval(total_value,staff_id,requisition_id)


