running = True


class Bus:
    def __init__(self, capacity: int, passengers: int, happy_passengers: int, unhappy_passengers: int):
        self.capacity = capacity
        self.passengers = passengers
        self.happy_passengers = happy_passengers
        self.unhappy_passengers = unhappy_passengers

    def get_happy_passenger_ratio(self) -> float:
        # If there are no unhappy passengers return 0.
        # Otherwise, return unhappy_passengers / happy_passengers
        return self.unhappy_passengers / self.happy_passengers if self.unhappy_passengers > 0 else 0


def get_int_input(message: str, minimum: int) -> int:
    """
    get_int_input requests an integer input from the
    user of a minimum value, specified by minimum.

    :param message: The message presented to the user
    :param minimum: Minimum allowed input
    :return: int
    """
    while True:
        try:
            input_num = int(input(message))

            if input_num < minimum:
                raise ValueError
            else:
                return input_num
        except:
            print("Invalid input. Please enter an integer of at least " + str(minimum) + ".")


def get_bool_input(message: str) -> bool:
    while True:
        user_input = input(message).upper()

        if user_input == "Y":
            return True
        elif user_input == "N":
            return False
        else:
            print("Invalid Input, please enter Y or N.")


def passengers_exiting(bus: Bus) -> None:
    if bus.passengers > 0:

        # Do while: passengers_exiting > passengers
        x = True
        while x:
            passengers_exiting = get_int_input("Enter number of passengers that exited: ", 0)

            # Is the number of passengers exiting greater than the number of passengers on the bus?
            if passengers_exiting > bus.passengers:
                print("There are not that many passengers on the bus! Please try again.")
            else:
                print("Passengers exiting: " + str(passengers_exiting))
                bus.passengers -= passengers_exiting
                x = False
    else:
        # No need to ask for input as there are no passengers on the bus.
        print("(AUTO) Passengers exiting: 0")


def passengers_entering(bus: Bus) -> None:
    entering_passengers = get_int_input("Enter number of passengers at stop: ", 0)

    # Get the remaining capacity on the bus
    remaining_capacity = bus.capacity - bus.passengers

    # If there are more passengers at the stop then capacity on the bus
    if entering_passengers > remaining_capacity:
        bus.passengers += remaining_capacity
        bus.happy_passengers += remaining_capacity

        entering_passengers -= remaining_capacity
        bus.unhappy_passengers += entering_passengers
    else:
        bus.passengers += entering_passengers
        bus.happy_passengers += entering_passengers


def main() -> None:
    global running
    bus = Bus(35, 0, 0, 0)

    # Get number of stops and route number
    print("\n\n--------------------------")
    route_number = get_int_input("Enter your route number: ", 0)
    bus_stops = get_int_input("Enter the number of bus stops: ", 3)

    # Loop through stops
    for i in range(1, bus_stops):
        txt = "----- Bus Stop {} ({}/{}) -----"
        print(txt.format(i, bus.passengers, bus.capacity))
        passengers_exiting()
        passengers_entering()

    # Final bus stop requires different structure
    print("----- Bus Stop " + str(bus_stops) + " (Final stop) -----")
    print("(AUTO) Passengers that exited: " + str(bus.passengers))
    passengers = 0

    # Final output
    txt = "\n----- Route Number: {}. Number of stops: {} -----"
    print(txt.format(route_number, bus_stops))
    print("Happy passengers: " + str(bus.happy_passengers))
    print("Unhappy passengers: " + str(bus.unhappy_passengers))
    print("Ratio of unhappy to happy customers: " + str(bus.get_happy_passenger_ratio()))


while running:
    main()

    # Ask if user wants to add another route
    print("\n\n")
    running = get_bool_input("Would you like to add another route? (Y/N): ")
