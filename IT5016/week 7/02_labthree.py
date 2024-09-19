
class RequestSystem:
    # Initialize the RequestSystem class
    def __init__(self):
        # Attributes to store requests and statistics
        self.requests = {}
        self.unique_id_counter = 1
        self.total_requests = 0
        self.approved_requests = 0
        self.pending_requests = 0
        self.not_approved_requests = 0

    def user_info(self):
        # Collect user information
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        email = input("Enter your email: ")
        
        print(f"User Information: Name - {name}, Age - {age}, Email - {email}")
        return name, age, email

    def request_details(self):
        # Collect request details
        items = []
        total_amount = 0

        print("Enter the request items (type 'done' to finish):")
        while True:
            item = input("Enter item name: ")
            if item.lower() == 'done':
                break
            try:
                cost = float(input(f"Enter cost for {item}: $"))
                items.append((item, cost))
                total_amount += cost
            except ValueError:
                print("Invalid cost. Please enter a valid number.")

        print(f"Total Amount: ${total_amount:.2f}")
        return items, total_amount

    def request_approval(self, total_amount):
        # Determine request approval status
        if total_amount < 150:
            status = "approved"
            self.approved_requests += 1
        else:
            status = "pending"
            self.pending_requests += 1
        
        return status

    def respond_request(self, request_id, response):
        # Allow a manager to respond to a pending request
        if request_id in self.requests and self.requests[request_id]['Status'] == "pending":
            if response.lower() == "approve":
                self.requests[request_id]['Status'] = "approved"
                self.approved_requests += 1
                self.pending_requests -= 1
            elif response.lower() == "not approve":
                self.requests[request_id]['Status'] = "not approved"
                self.not_approved_requests += 1
                self.pending_requests -= 1
            else:
                print("Invalid response. Please enter 'approve' or 'not approve'.")
        else:
            print("Invalid request ID or the request is not pending.")

    def display_request(self):
        # Display all request objects
        print("\n--- All Requests ---")
        for request_id, details in self.requests.items():
            print(f"Request ID: {request_id}, Name: {details['Name']}, Total: ${details['Total']:.2f}, Status: {details['Status']}")

    def request_statistic(self):
        # Display statistical information about the requests
        print("\n--- Request Statistics ---")
        print(f"Total Requests Submitted: {self.total_requests}")
        print(f"Total Approved Requests: {self.approved_requests}")
        print(f"Total Pending Requests: {self.pending_requests}")
        print(f"Total Not Approved Requests: {self.not_approved_requests}")

    def submit_request(self):
        # Collect user info and request details, then submit the request
        name, age, email = self.user_info()
        items, total_amount = self.request_details()
        status = self.request_approval(total_amount)

        # Store the request
        request_id = self.unique_id_counter
        self.requests[request_id] = {
            'Name': name,
            'Age': age,
            'Email': email,
            'Items': items,
            'Total': total_amount,
            'Status': status
        }
        self.unique_id_counter += 1
        self.total_requests += 1

        print(f"Request submitted successfully with ID: {request_id}, Status: {status}")


# Example Usage
system = RequestSystem()

# Loop to interact with the user
while True:
    print("\n1. Submit a Request")
    print("2. Respond to a Request")
    print("3. Display All Requests")
    print("4. Show Request Statistics")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        system.submit_request()
    elif choice == '2':
        request_id = int(input("Enter Request ID to respond: "))
        response = input("Enter response (approve/not approve): ")
        system.respond_request(request_id, response)
    elif choice == '3':
        system.display_request()
    elif choice == '4':
        system.request_statistic()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")


# class RequestSystem:
#     # Initialize the class with necessary attributes
#     def __init__(self):
#         self.requests = []  # List to store all requests
#         self.request_id_counter = 1  # Unique ID counter for requests

#     # Method to collect user information
#     def user_info(self, name, age, email):
#         self.name = name
#         self.age = age
#         self.email = email
#         print(f"User information collected: Name - {name}, Age - {age}, Email - {email}")

#     # Method to accept request details and calculate total cost
#     def request_details(self, items):
#         total_cost = sum(item['cost'] for item in items)
#         request = {
#             'id': self.request_id_counter,
#             'name': self.name,
#             'items': items,
#             'total_cost': total_cost,
#             'status': 'pending'
#         }
#         self.requests.append(request)
#         self.request_id_counter += 1
#         print(f"Request submitted for {self.name}. Total: ${total_cost}")
#         return total_cost, items

#     # Method to approve or mark requests as pending based on total amount
#     def request_approval(self):
#         for request in self.requests:
#             if request['total_cost'] < 150:
#                 request['status'] = 'approved'
#             else:
#                 request['status'] = 'pending'
#             print(f"Request ID {request['id']} has been {request['status']}")

#     # Method for manager to respond to a request
#     def respond_request(self, request_id, approval):
#         for request in self.requests:
#             if request['id'] == request_id:
#                 if approval:
#                     request['status'] = 'approved'
#                 else:
#                     request['status'] = 'not approved'
#                 print(f"Manager responded to request ID {request_id}: {request['status']}")
#                 break

#     # Method to display all requests and their details
#     def display_request(self):
#         for request in self.requests:
#             print(f"Request ID: {request['id']}, Name: {request['name']}, Total: ${request['total_cost']}, Status: {request['status']}")

#     # Method to display statistics of requests
#     def request_statistic(self):
#         total_requests = len(self.requests)
#         approved_requests = sum(1 for r in self.requests if r['status'] == 'approved')
#         pending_requests = sum(1 for r in self.requests if r['status'] == 'pending')
#         not_approved_requests = sum(1 for r in self.requests if r['status'] == 'not approved')

#         print(f"Total requests: {total_requests}")
#         print(f"Approved requests: {approved_requests}")
#         print(f"Pending requests: {pending_requests}")
#         print(f"Not approved requests: {not_approved_requests}")



        
