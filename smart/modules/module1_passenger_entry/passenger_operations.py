from modules.module1_passenger_entry.passenger import Passenger
from modules.module1_passenger_entry.passenger_data import passenger_list


class PassengerOperations:

    # Add passenger manually
    def add_manual_passenger(self):

        print("\n===== Enter Passenger Details =====")

        while True:

            passenger_id = input("Enter Passenger ID : ")

            if passenger_id.strip() == "":
                print("Invalid Passenger ID")
            else:
                break

        while True:

            name = input("Enter Passenger Name : ")

            if name.strip() == "":
                print("Invalid Name")
            else:
                break

        while True:

            try:
                age = int(input("Enter Passenger Age : "))

                if age <= 0:
                    print("Invalid Age")
                else:
                    break

            except ValueError:
                print("Enter Numbers Only")

        while True:

            try:
                platform = int(input("Enter Platform Number : "))

                if platform <= 0:
                    print("Invalid Platform")
                else:
                    break

            except ValueError:
                print("Enter Numbers Only")

        ticket_number = input("Enter Ticket Number : ")

        while True:

            try:
                people_count = int(input("Enter People Count : "))

                if people_count <= 0:
                    print("Invalid People Count")
                else:
                    break

            except ValueError:
                print("Enter Numbers Only")

        new_passenger = {

            "passenger_id": passenger_id,
            "name": name,
            "age": age,
            "platform": platform,
            "ticket_number": ticket_number,
            "people_count": people_count
        }

        passenger_list.append(new_passenger)

        print("\nPassenger Added Successfully")

    # Use existing data
    def use_existing_data(self):

        print("\n===== Existing Passenger Data =====")

        for passenger in passenger_list:

            passenger_obj = Passenger(

                passenger["passenger_id"],
                passenger["name"],
                passenger["age"],
                passenger["platform"],
                passenger["ticket_number"],
                passenger["people_count"]

            )

            passenger_obj.display_passenger()

    # Display all passengers
    def display_all_passengers(self):

        print("\n===== All Passenger Records =====")

        for passenger in passenger_list:

            print("\n----------------------------")

            print("Passenger ID  :", passenger["passenger_id"])
            print("Name          :", passenger["name"])
            print("Age           :", passenger["age"])
            print("Platform      :", passenger["platform"])
            print("Ticket Number :", passenger["ticket_number"])
            print("People Count  :", passenger["people_count"])

    # Search passenger
    def search_passenger(self):

        search_id = input("\nEnter Passenger ID to Search : ")

        found = False

        for passenger in passenger_list:

            if passenger["passenger_id"] == search_id:

                print("\nPassenger Found")

                print("----------------------")

                print("Passenger ID  :", passenger["passenger_id"])
                print("Name          :", passenger["name"])
                print("Age           :", passenger["age"])
                print("Platform      :", passenger["platform"])
                print("Ticket Number :", passenger["ticket_number"])
                print("People Count  :", passenger["people_count"])

                found = True
                break

        if found == False:

            print("\nPassenger Not Found")

    # Total passenger count
    def total_passenger_count(self):

        total = len(passenger_list)

        print("\nTotal Passengers :", total)

    # Report Generator
    def report_generator(self):

        print("\n===== Crowd Report Generator =====")

        for passenger in passenger_list:

            people_count = passenger["people_count"]

            print("\nPlatform :", passenger["platform"])
            print("People Count :", people_count)

            if people_count < 500:

                print("Status : SAFE ZONE")

            elif people_count >= 500 and people_count < 700:

                print("Status : MODERATE CROWD")

            else:

                print("Status : HIGH RISK")
                print("DO NOT GIVE PLATFORM TICKET")

    # Passenger menu
    def passenger_menu(self):

        while True:

            print("\n========== Passenger Entry Module ==========")

            print("1. Enter Passenger Data Manually")
            print("2. Use Existing Passenger Data")
            print("3. Display All Passengers")
            print("4. Search Passenger")
            print("5. Show Total Passenger Count")
            print("6. Report Generator")
            print("7. Exit Passenger Module")

            choice = input("\nEnter your choice : ")

            if choice == "1":

                self.add_manual_passenger()

            elif choice == "2":

                self.use_existing_data()

            elif choice == "3":

                self.display_all_passengers()

            elif choice == "4":

                self.search_passenger()

            elif choice == "5":

                self.total_passenger_count()

            elif choice == "6":

                self.report_generator()

            elif choice == "7":

                print("\nExiting Passenger Module...")
                break

            else:

                print("\nInvalid Choice! Enter Again")