class QueueManager:

    def __init__(self):

        self.queue = []

    # Add passenger to queue
    def add_passenger(self, passenger_name):

        self.queue.append(passenger_name)

        print(f"\n{passenger_name} added to queue")

    # Remove passenger from queue
    def remove_passenger(self):

        if len(self.queue) == 0:

            print("\nQueue is Empty")

        else:

            removed_passenger = self.queue.pop(0)

            print(f"\n{removed_passenger} removed from queue")

    # Display queue
    def display_queue(self):

        print("\n===== Passenger Queue =====")

        if len(self.queue) == 0:

            print("Queue is Empty")

        else:

            position = 1

            for passenger in self.queue:

                print(f"{position}. {passenger}")

                position += 1

    # Queue count
    def queue_count(self):

        total = len(self.queue)

        print("\nTotal Passengers in Queue :", total)

        return total