from modules.module1_passenger_entry.passenger_data import passenger_list


class ReportGenerator:

    # Generate crowd report
    def generate_report(self):

        print("\n===== PLATFORM CROWD REPORT =====")

        for passenger in passenger_list:

            platform = passenger["platform"]
            people_count = passenger["people_count"]

            print("\n--------------------------------")
            print("Platform Number :", platform)
            print("People Count    :", people_count)

            # Crowd Monitoring Logic
            if people_count < 500:

                print("Crowd Status : SAFE ZONE")

            elif people_count >= 500 and people_count < 700:

                print("Crowd Status : MODERATE CROWD")

            else:

                print("Crowd Status : HIGH RISK")
                print("WARNING : DO NOT GIVE PLATFORM TICKET")