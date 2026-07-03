class Ticket:

    def __init__(self, ticket_number, passenger_id):

        self.ticket_number = ticket_number
        self.passenger_id = passenger_id

    def display_ticket(self):

        print("\n===== Ticket Details =====")

        print("Ticket Number :", self.ticket_number)
        print("Passenger ID  :", self.passenger_id)