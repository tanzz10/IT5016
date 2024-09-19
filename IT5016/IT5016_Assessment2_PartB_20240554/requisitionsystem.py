"""
Requisition System
Author: Tania Tanisha Bhan
"""
class RequisitionSystem:
    unique_id = 10000  
    total_requisitions = 0
    approved_count = 0
    pending_count = 0
    not_approved_count = 0
    all_requisitions = []  # store all requisition instances

    def __init__(self, date='', staff_id='', staff_name='', status="Pending"):
        self.date = date
        self.staff_id = staff_id
        self.staff_name = staff_name
        self.status = status
        self.requisition_id = RequisitionSystem.unique_id + 1
        RequisitionSystem.unique_id += 1
        RequisitionSystem.total_requisitions += 1  
        RequisitionSystem.all_requisitions.append(self)  

    def staff_info(self):
        self.date = input("Enter today's date:")
        self.staff_id = input("Enter your Staff ID:")
        self.staff_name = input("Enter your name:")

    def requisition_details(self):
        total_value = 0
        while True:
            price_of_item = input("Enter each item name with a cost (e.g., Tea $20), or 'finish' to stop:")
            if price_of_item.lower() == 'finish':
                break
            try:
                item_name, price = price_of_item.rsplit(maxsplit=1)
                item_name = str(item_name)
                price = float(price.replace("$", ""))
                total_value += price
            except ValueError:
                print("Invalid input. Please follow the format (e.g., Tea $20).")
        return total_value

    def requisition_approval(self, total_value):
        if total_value < 500:
            self.status = "Approved"
            reference_number = str(self.staff_id) + str(self.requisition_id)[-3:]
            RequisitionSystem.approved_count += 1  
        else:
            self.status = "Pending"
            reference_number = "Not Available"
            RequisitionSystem.pending_count += 1  

        print(f"Requisition Approval:")
        print(f"Total: ${total_value:.2f}")
        print(f"Status: {self.status}")
        print(f"Approval Reference Number: {reference_number}")

    def respond_requisition(self, total_value):
        if total_value > 500:
            self.status = input("Enter Approved or Not Approved: ")
            if self.status == "Approved":
                RequisitionSystem.approved_count += 1
            else:
                RequisitionSystem.not_approved_count += 1
        else:
            self.status = "Approved"

        print(f"Status: {self.status}")

    def display_requisitions(self, total_value, reference_number):
        print(f"\nPrinting Requisitions:")
        print(f"Date: {self.date}")
        print(f"Requisition ID: {self.requisition_id}")
        print(f"Staff ID: {self.staff_id}")
        print(f"Staff Name: {self.staff_name}")
        print(f"Total: ${total_value:.2f}")
        print(f"Status: {self.status}")
        print(f"Approval Reference Number: {reference_number}")

    def display_all_requisitions(self):
        print("\n--- Displaying All Requisitions ---")
        for requisition in RequisitionSystem.all_requisitions:
            reference_number = "Not Available" if requisition.status != "Approved" else str(requisition.staff_id) + str(requisition.requisition_id)[-3:]
            total_value = 0  
            requisition.display_requisitions(total_value, reference_number)

    def requisition_statistic(self):
        # Display the statistics
        print(f"\n--- Displaying Requisition Statistics ---")
        print(f"Total number of requisitions submitted: {RequisitionSystem.total_requisitions}")
        print(f"Total number of approved requisitions: {RequisitionSystem.approved_count}")
        print(f"Total number of pending requisitions: {RequisitionSystem.pending_count}")
        print(f"Total number of not approved requisitions: {RequisitionSystem.not_approved_count}")


def main():
    while True:
        add_staff = input("Do you want to add a staff requisition? (yes/no): ").lower()
        if add_staff == 'no':
            break
        req = RequisitionSystem()
        req.staff_info()
        total_value = req.requisition_details()
        req.requisition_approval(total_value)
        req.respond_requisition(total_value)
        reference_number = "Not Available" if req.status != "Approved" else str(req.staff_id) + str(req.requisition_id)[-3:]
        req.display_requisitions(total_value, reference_number)

    RequisitionSystem().requisition_statistic()
    RequisitionSystem().display_all_requisitions()

main()