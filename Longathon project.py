import json

# Complaint class to store complaint details
class Complaint:
    def __init__(self, complaint_id, enrollment_id, title, description, status, emergency=False):
        self.complaint_id = complaint_id
        self.enrollment_id = enrollment_id
        self.title = title
        self.description = description
        self.status = status
        self.emergency = emergency  # New attribute for emergency status

    def to_dict(self):
        # Convert complaint object to dictionary (for saving to JSON)
        return {
            "complaint_id": self.complaint_id,
            "enrollment_id": self.enrollment_id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "emergency": self.emergency  # Add emergency status to dictionary
        }

# User class to store user details (now based on enrollment_id)
class User:
    def __init__(self, enrollment_id, name):
        self.enrollment_id = enrollment_id  # Enrollment ID is used here
        self.name = name

    def to_dict(self):
        # Convert user object to dictionary (for saving to JSON)
        return {
            "enrollment_id": self.enrollment_id,
            "name": self.name
        }

# Complaint Management System class
class ComplaintManagementSystem:
    ADMIN_PASSWORD = "admin123"  # Set a default admin password

    def __init__(self):
        self.complaints = []  # Store all complaints
        self.users = {}  # A dictionary to store users by their enrollment_id
        self.complaint_id_tracker = {}  # Track last complaint ID for each user
        self.load_data()  # Load data from file when initializing

    def register_user(self, enrollment_id, name):
        # Register a user with their enrollment_id
        if enrollment_id in self.users:
            print(f"User with Enrollment ID {enrollment_id} already exists.")
            return None
        user = User(enrollment_id, name)
        self.users[enrollment_id] = user
        self.complaint_id_tracker[enrollment_id] = 0  # Initialize complaint ID counter for this user
        print(f"User registered successfully! Your Enrollment ID is: {enrollment_id}")
        self.save_data()  # Save data to file
        return enrollment_id

    def login_user(self, enrollment_id):
        # Login the user using their enrollment_id
        if enrollment_id in self.users:
            print(f"Welcome back, {self.users[enrollment_id].name}!")
            return enrollment_id
        else:
            print("User not found. Please register first.")
            return None

    def register_complaint(self, enrollment_id, title, description, emergency=False):
        # Check if the user exists and initialize their complaint ID if needed
        if enrollment_id not in self.complaint_id_tracker:
            self.complaint_id_tracker[enrollment_id] = 0  # Initialize if missing

        # Register a complaint for the user with the given enrollment_id
        complaint_id = self.complaint_id_tracker[enrollment_id] + 1
        status = "Pending"
        complaint = Complaint(complaint_id, enrollment_id, title, description, status, emergency)
        self.complaints.append(complaint)
        self.complaint_id_tracker[enrollment_id] = complaint_id  # Update the last used complaint ID for this user
        print(f"Complaint registered successfully! Your Complaint ID is: {complaint_id}")
        self.save_data()  # Save data to file

    def view_complaints(self, enrollment_id):
        # View all complaints of a specific user based on their enrollment_id
        user_complaints = [complaint for complaint in self.complaints if complaint.enrollment_id == enrollment_id]
        if not user_complaints:
            print("No complaints registered for this user.")
        else:
            # Sort complaints: Emergency complaints first, then others
            user_complaints.sort(key=lambda x: (not x.emergency, x.complaint_id))

            for complaint in user_complaints:
                print(f"Complaint ID: {complaint.complaint_id}")
                print(f"Title: {complaint.title}")
                print(f"Description: {complaint.description}")
                print(f"Status: {complaint.status}")
                print(f"Emergency: {'Yes' if complaint.emergency else 'No'}")
                print("-----------------------------")

    def update_complaint_status(self, complaint_id, new_status):
        # Update the status of a specific complaint based on complaint_id
        for complaint in self.complaints:
            if complaint.complaint_id == complaint_id:
                complaint.status = new_status
                print(f"Complaint ID {complaint_id} status updated to '{new_status}' successfully!")
                self.save_data()  # Save data to file after update
                return
        print("Complaint not found.")

    # Admin Functions
    def admin_login(self):
        # Authenticate admin with a password
        password = input("Enter admin password: ")
        return password == self.ADMIN_PASSWORD

    def view_all_complaints(self):
        # View all complaints in the system
        if not self.complaints:
            print("No complaints have been registered.")
            return
        
        # Sort complaints: Emergency complaints first, then others by ID
        all_complaints = sorted(self.complaints, key=lambda x: (not x.emergency, x.complaint_id))

        print("All Complaints:")
        for complaint in all_complaints:
            print(f"Complaint ID: {complaint.complaint_id}")
            print(f"Enrollment ID: {complaint.enrollment_id}")
            print(f"Title: {complaint.title}")
            print(f"Description: {complaint.description}")
            print(f"Status: {complaint.status}")
            print(f"Emergency: {'Yes' if complaint.emergency else 'No'}")
            print("-----------------------------")

    def update_any_complaint_status(self, complaint_id, new_status):
        # Update the status of any complaint by complaint_id
        for complaint in self.complaints:
            if complaint.complaint_id == complaint_id:
                complaint.status = new_status
                print(f"Complaint ID {complaint_id} status updated to '{new_status}' successfully!")
                self.save_data()  # Save data to file after update
                return
        print("Complaint not found.")

    def delete_complaint(self, complaint_id):
        # Delete a specific complaint by complaint_id
        for i, complaint in enumerate(self.complaints):
            if complaint.complaint_id == complaint_id:
                del self.complaints[i]
                print(f"Complaint ID {complaint_id} deleted successfully!")
                self.save_data()  # Save data to file after deletion
                return
        print("Complaint not found.")

    def save_data(self):
        # Save users and complaints data to a file (in JSON format)
        with open("complaint_data.json", "w") as file:
            data = {
                "users": {key: user.to_dict() for key, user in self.users.items()},
                "complaints": [complaint.to_dict() for complaint in self.complaints],
                "complaint_id_tracker": self.complaint_id_tracker  # Save the complaint ID tracker
            }
            json.dump(data, file, indent=4)

    def load_data(self):
        # Load users and complaints data from a file (if it exists)
        try:
            with open("complaint_data.json", "r") as file:
                data = json.load(file)
                self.users = {key: User(**user_data) for key, user_data in data["users"].items()}
                self.complaints = [Complaint(**complaint_data) for complaint_data in data["complaints"]]
                self.complaint_id_tracker = data.get("complaint_id_tracker", {})  # Load the complaint ID tracker
        except FileNotFoundError:
            print("No previous data found, starting fresh.")

# Main function to run the Complaint Management System
def main():
    cms = ComplaintManagementSystem()

    print("Welcome to the Complaint Management System!")
    
    while True:
        print("\nMain Menu:")
        print("1. Register as New Student")
        print("2. Student Login")
        print("3. Admin Login")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            enrollment_id = input("Enter a unique Enrollment ID: ")
            name = input("Enter your name: ")
            cms.register_user(enrollment_id, name)
        
        elif choice == "2":
            student_interface(cms)
        
        elif choice == "3":
            if cms.admin_login():
                print("Admin login successful!")
                admin_interface(cms)
            else:
                print("Incorrect password.")
        
        elif choice == "4":
            print("Exiting the Complaint Management System...")
            break
        else:
            print("Invalid choice. Please try again.")

def student_interface(cms):
    enrollment_id = input("Enter your Enrollment ID: ")
    if cms.login_user(enrollment_id):
        while True:
            print("\nStudent Interface:")
            print("1. Register Complaint")
            print("2. View Complaint History")
            print("3. Update Complaint Status")
            print("4. Logout")
            choice = input("Enter your choice: ")

            if choice == "1":
                title = input("Enter complaint title: ")
                description = input("Enter complaint description: ")
                emergency = input("Is this an emergency complaint? (yes/no): ").lower() == "yes"
                cms.register_complaint(enrollment_id, title, description, emergency)
            
            elif choice == "2":
                cms.view_complaints(enrollment_id)
            
            elif choice == "3":
                try:
                    complaint_id = int(input("Enter Complaint ID to update: "))
                    new_status = input("Enter new status (e.g., 'Resolved', 'In Progress'): ")
                    cms.update_complaint_status(complaint_id, new_status)
                except ValueError:
                    print("Invalid Complaint ID. Please enter a numeric value.")
            
            elif choice == "4":
                print("Logging out...")
                break
            
            else:
                print("Invalid choice. Please try again.")

def admin_interface(cms):
    while True:
        print("\nAdmin Interface:")
        print("1. View All Complaints")
        print("2. Update Complaint Status")
        print("3. Delete a Complaint")
        print("4. Exit Admin Interface")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            cms.view_all_complaints()
        
        elif choice == "2":
            try:
                complaint_id = int(input("Enter Complaint ID to update: "))
                new_status = input("Enter new status (e.g., 'Resolved', 'In Progress'): ")
                cms.update_any_complaint_status(complaint_id, new_status)
            except ValueError:
                print("Invalid Complaint ID. Please enter a numeric value.")
        
        elif choice == "3":
            try:
                complaint_id = int(input("Enter Complaint ID to delete: "))
                cms.delete_complaint(complaint_id)
            except ValueError:
                print("Invalid Complaint ID. Please enter a numeric value.")
        
        elif choice == "4":
            print("Exiting Admin Interface...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
