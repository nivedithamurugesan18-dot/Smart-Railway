from modules.module1_passenger_entry.passenger_operations import PassengerOperations

from modules.module2_ticket_verification.ticket_operations import TicketOperations

from modules.module3_crowd_analysis.crowd_analyzer import CrowdAnalyzer


def main():

    passenger_obj = PassengerOperations()

    ticket_obj = TicketOperations()

    crowd_obj = CrowdAnalyzer()

    while True:

        print("\n======================================")
        print(" SMART RAILWAY CROWD MANAGEMENT SYSTEM ")
        print("======================================")

        print("\n1. Passenger Entry Module")
        print("2. Ticket Verification Module")
        print("3. Crowd Analysis Module")
        print("4. Exit Project")

        choice = input("\nEnter your choice : ")

        if choice == "1":

            passenger_obj.passenger_menu()

        elif choice == "2":

            ticket_obj.ticket_menu()

        elif choice == "3":

            crowd_obj.crowd_menu()

        elif choice == "4":

            print("\nProject Closed Successfully")
            break

        else:

            print("\nInvalid Choice! Enter Again")


main()