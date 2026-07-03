from modules.module3_crowd_analysis.queue_manager import QueueManager
from modules.module3_crowd_analysis.crowd_data import queue_data


class CrowdAnalyzer:

    def __init__(self):

        self.queue_manager = QueueManager()

    # Use existing crowd data
    def use_existing_data(self):

        print("\n===== Existing Crowd Data =====")

        for data in queue_data:

            print("\n----------------------------")

            print("Platform Number :", data["platform"])
            print("Passenger Count :", data["passenger_count"])
            print("Service Time    :", data["service_time"])

    # Add passenger to queue
    def add_passenger_to_queue(self):

        passenger_name = input("\nEnter Passenger Name : ")

        self.queue_manager.add_passenger(passenger_name)

    # Remove passenger from queue
    def remove_passenger_from_queue(self):

        self.queue_manager.remove_passenger()

    # Display queue
    def display_queue(self):

        self.queue_manager.display_queue()

    # Analyze crowd level
    def analyze_crowd(self):

        print("\n===== Crowd Analysis =====")

        for data in queue_data:

            platform = data["platform"]
            passenger_count = data["passenger_count"]
            service_time = data["service_time"]

            waiting_time = passenger_count * service_time

            print("\n----------------------------")

            print("Platform Number :", platform)
            print("Passenger Count :", passenger_count)
            print("Waiting Time    :", waiting_time, "Minutes")

            # Crowd Level Logic
            if passenger_count <= 20:

                print("Crowd Level : LOW CROWD")

            elif passenger_count > 20 and passenger_count <= 50:

                print("Crowd Level : MODERATE CROWD")

            else:

                print("Crowd Level : HIGH CROWD")
                print("WARNING : PLATFORM OVERCROWDED")

    # Crowd menu
    def crowd_menu(self):

        while True:

            print("\n========== Crowd Analysis Module ==========")

            print("1. Add Passenger to Queue")
            print("2. Remove Passenger from Queue")
            print("3. Display Queue")
            print("4. Use Existing Crowd Data")
            print("5. Analyze Crowd Level")
            print("6. Show Queue Count")
            print("7. Exit Crowd Module")

            choice = input("\nEnter your choice : ")

            if choice == "1":

                self.add_passenger_to_queue()

            elif choice == "2":

                self.remove_passenger_from_queue()

            elif choice == "3":

                self.display_queue()

            elif choice == "4":

                self.use_existing_data()

            elif choice == "5":

                self.analyze_crowd()

            elif choice == "6":

                self.queue_manager.queue_count()

            elif choice == "7":

                print("\nExiting Crowd Module...")
                break

            else:

                print("\nInvalid Choice")