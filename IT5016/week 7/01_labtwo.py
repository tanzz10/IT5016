# class Student:
#   def __init__(self,student_id,last_name,programme):
#     self.student_id = student_id
#     self.last_name = last_name
#     self.programme = programme

# class Club:
#   def __init__(self):
#     self.members = []
#     self.withdrawn_students = []
#     self.next_membership_id = 1

#     def register_student(self, student_id, last_name, programme):
#         new_student = Student(student_id, last_name, programme)
#         new_student.membership_id = self.next_membership_id
#         self.next_membership_id += 1
#         self.members.append(new_student)
#         print(f"Student {new_student.last_name} registered successfully with Membership ID {new_student.membership_id}.")

#     def withdraw_student(self, membership_id, last_name):
#         for student in self.members:
#             if student.membership_id == membership_id and student.last_name == last_name:
#                 self.members.remove(student)
#                 self.withdrawn_students.append(student)
#                 print(f"Student {student.last_name} with Membership ID {membership_id} has been withdrawn.")
#                 return
#         print(f"No matching student found with Membership ID {membership_id} and Last Name {last_name}.")

#     def display_statistics(self):
#         total_members = len(self.members)
#         diploma_count = sum(1 for student in self.members if student.programme == "Diploma")
#         bachelor_count = sum(1 for student in self.members if student.programme == "Bachelor")
#         withdrawn_count = len(self.withdrawn_students)

#         print("\n--- Club Membership Statistics ---")
#         print(f"Total Registered Members: {total_members}")
#         print(f"Number of Diploma Programme Members: {diploma_count}")
#         print(f"Number of Bachelor Programme Members: {bachelor_count}")
#         print(f"Number of Withdrawn Students: {withdrawn_count}")


# club = Club()
# club.register_student("1001", "Bhan", "Diploma")
# club.register_student("1002", "Khan", "Bachelor")
# club.register_student("1003", "James", "Diploma")
# club.withdraw_student(2, "Khan")
# club.display_statistics()


class WhitecliffeStudentsClub:
    def __init__(self):
        # Initialize counters and storage
        self.members = {}
        self.next_membership_id = 1
        self.registered_members_count = 0
        self.diploma_students_count = 0
        self.bachelor_students_count = 0
        self.withdrawn_students_count = 0

    def register_student(self):
        # Ask for student information
        student_id = input("Enter Student ID: ")
        last_name = input("Enter Student Last Name: ")
        programme = input("Enter Student Programme (Diploma or Bachelor): ")

        # Validate the programme input
        if programme.lower() not in ['diploma', 'bachelor']:
            print("Invalid programme. Please enter either 'Diploma' or 'Bachelor'.")
            return

        # Generate a new membership ID
        membership_id = self.next_membership_id
        self.next_membership_id += 1

        # Store member information
        self.members[membership_id] = {
            'Student ID': student_id,
            'Last Name': last_name,
            'Programme': programme,
        }

        # Update counters
        self.registered_members_count += 1
        if programme.lower() == 'diploma':
            self.diploma_students_count += 1
        else:
            self.bachelor_students_count += 1

        print(f"Student {last_name} has been successfully registered with Membership ID: {membership_id}")

    def withdraw_student(self):
        # Ask for withdrawal information
        membership_id = int(input("Enter Membership ID to withdraw: "))
        last_name = input("Enter Student Last Name: ")

        # Check if membership ID exists
        if membership_id not in self.members:
            print("Invalid Membership ID.")
            return

        # Check if last name matches
        if self.members[membership_id]['Last Name'] != last_name:
            print("Last name does not match our records.")
            return

        # Remove the student and update counters
        programme = self.members[membership_id]['Programme']
        del self.members[membership_id]
        self.registered_members_count -= 1
        self.withdrawn_students_count += 1

        if programme.lower() == 'diploma':
            self.diploma_students_count -= 1
        else:
            self.bachelor_students_count -= 1

        print(f"Student {last_name} with Membership ID {membership_id} has been successfully withdrawn.")

    def display_statistics(self):
        # Display the statistics
        print("\n--- Membership Statistics ---")
        print(f"Total Registered Members: {self.registered_members_count}")
        print(f"Total Diploma Programme Students: {self.diploma_students_count}")
        print(f"Total Bachelor Programme Students: {self.bachelor_students_count}")
        print(f"Total Withdrawn Students: {self.withdrawn_students_count}\n")


# Example Usage
club = WhitecliffeStudentsClub()

# Loop to interact with the user
while True:
    print("\n1. Register a Student")
    print("2. Withdraw a Student")
    print("3. Display Membership Statistics")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        club.register_student()
    elif choice == '2':
        club.withdraw_student()
    elif choice == '3':
        club.display_statistics()
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")

     

  
