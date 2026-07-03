class Passenger:

    def __init__(
        self,
        passenger_id,
        name,
        age,
        platform,
        ticket_number,
        people_count
    ):

        self.passenger_id = passenger_id
        self.name = name
        self.age = age
        self.platform = platform
        self.ticket_number = ticket_number
        self.people_count = people_count

    def display_passenger(self):

        print("\n===== Passenger Details =====")

        print("Passenger ID  :", self.passenger_id)
        print("Name          :", self.name)
        print("Age           :", self.age)
        print("Platform      :", self.platform)
        print("Ticket Number :", self.ticket_number)
        print("People Count  :", self.people_count)