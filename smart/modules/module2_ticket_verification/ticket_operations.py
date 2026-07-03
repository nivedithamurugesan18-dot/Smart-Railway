from modules.module2_ticket_verification.ticket import Ticket
from modules.module2_ticket_verification.ticket_data import ticket_records


class TicketOperations:

    # Add ticket manually
    def add_manual_ticket(self):

        print("\n===== Enter Ticket Details =====")

        ticket_number = input("Enter Ticket Number : ")
        passenger_id = input("Enter Passenger ID : ")

        ticket_records[ticket_number] = passenger_id

        print("\nTicket Added Successfully")

    # Use existing ticket data
    def use_existing_data(self):

        print("\n===== Existing Ticket Data =====")

        for ticket_number, passenger_id in ticket_records.items():

            ticket_obj = Ticket(ticket_number, passenger_id)

            ticket_obj.display_ticket()

    # Recursive ticket verification
    def recursive_ticket_check(self, ticket_list, target_ticket, index=0):

        if index >= len(ticket_list):

            return False

        if ticket_list[index] == target_ticket:

            return True

        return self.recursive_ticket_check(
            ticket_list,
            target_ticket,
            index + 1
        )

    # Verify ticket
    def verify_ticket(self):

        ticket_number = input("\nEnter Ticket Number to Verify : ")

        ticket_list = list(ticket_records.keys())

        result = self.recursive_ticket_check(
            ticket_list,
            ticket_number
        )

        if result:

            print("\nTicket Verified Successfully")
            print("Passenger Allowed")

        else:

            print("\nInvalid Ticket")
            print("Passenger Not Allowed")

    # Display all tickets
    def display_all_tickets(self):

        print("\n===== All Ticket Records =====")

        for ticket_number, passenger_id in ticket_records.items():

            print("\n----------------------")
            print("Ticket Number :", ticket_number)
            print("Passenger ID  :", passenger_id)

    # Total ticket count
    def total_ticket_count(self):

        total = len(ticket_records)

        print("\nTotal Tickets :", total)

    # Ticket menu
    def ticket_menu(self):

        while True:

            print("\n========== Ticket Verification Module ==========")

            print("1. Enter Ticket Data Manually")
            print("2. Use Existing Ticket Data")
            print("3. Verify Ticket")
            print("4. Display All Tickets")
            print("5. Show Total Ticket Count")
            print("6. Exit Ticket Module")

            choice = input("\nEnter your choice : ")

            if choice == "1":

                self.add_manual_ticket()

            elif choice == "2":

                self.use_existing_data()

            elif choice == "3":

                self.verify_ticket()

            elif choice == "4":

                self.display_all_tickets()

            elif choice == "5":

                self.total_ticket_count()

            elif choice == "6":

                print("\nExiting Ticket Module...")
                break

            else:

                print("\nInvalid Choice")