running = True


class Bus:
    def __init__(self, capacity: int, passengers: int, happy_passengers: int, unhappy_passengers: int):
        self._capacity = capacity
        self._passengers = passengers
        self._happy_passengers = happy_passengers
        self._unhappy_passengers = unhappy_passengers

    def get_happy_passenger_ratio(self) -> float:
        # If there are no unhappy passengers return 0.
        # Otherwise, return unhappy_passengers / happy_passengers
        return self._unhappy_passengers / self._happy_passengers if self._unhappy_passengers > 0 else 0

    def get_capacity(self) -> int:
        return self._capacity

    def get_passengers(self) -> int:
        return self._passengers

    def add_passengers(self, passengers: int) -> None:
        # Guard clause, there is no need to continue if passengers are <= 0
        if passengers <= 0:
            return

        # Calculate the overfull amount, I.e. the number of passengers unable
        # to enter the bus due to capacity limitations.
        if passengers + self._passengers < self._capacity:
            overfill = 0
        else:
            overfill = passengers + self._passengers - self._capacity

        self._passengers += passengers - overfill
        self._happy_passengers += passengers - overfill
        self._unhappy_passengers += overfill

    def set_passengers(self, passengers: int):
        """
        set_passengers sets the local variable _passengers to the inputted value passengers.

        WARNING: This function does not contain protections for preventing going over _capacity or going under 0.
                 Use bus.add_passengers to prevent this.

        :param passengers: New Value
        """
        self._passengers = passengers

    def get_happy_passengers(self):
        return self._happy_passengers

    def get_unhappy_passengers(self):
        return self._unhappy_passengers


def get_int_input(message: str, minimum: int = None, maximum: int = None) -> int:
    """
    get_int_input requests an integer input from the
    user of a minimum value, specified by minimum.

    :param message: The message presented to the user
    :param minimum: Minimum allowed input
    :param maximum: Maximum allowed input
    :return: int
    """
    while True:
        try:
            input_num = int(input(message))

            if minimum is not None and input_num < minimum:
                print("Invalid input. Please enter an integer of at least " + str(minimum) + ".")
            elif maximum is not None and input_num > maximum:
                print("Invalid input. Please enter an integer of at least " + str(maximum) + ".")
            else:
                return input_num
        except:
            print("Invalid input. Please enter an integer")


def get_bool_input(message: str) -> bool:
    """
    get_bool_input requests a boolean input from the user.

    :param message: The message presented to the user
    :return: bool
    """
    while True:
        user_input = input(message).lower()

        if user_input == "y":
            return True
        elif user_input == "n":
            return False
        else:
            print("Invalid Input, please enter Y or N.")


def request_exiting_passengers(bus: Bus) -> None:
    """
    request_exiting_passengers requests an integer input from the user
    specifying the amount of passengers exiting the bus.

    :param bus: The bus object this function will perform on.
    """
    if bus.get_passengers() > 0:
        passengers_exiting = get_int_input("Enter number of passengers that exited: ", 0, bus.get_passengers())
        bus.set_passengers(bus.get_passengers() - passengers_exiting)
    else:
        # No need to ask for input as there are no passengers on the bus.
        print("(AUTO) Passengers exiting: 0")


def request_passengers_entering(bus: Bus) -> None:
    """
    request_passengers_entering requests an integer from the user specifying
    the number of passengers entering the bus.

    :param bus: The bus object this function will perform on.
    """
    entering_passengers = get_int_input("Enter number of passengers at stop: ", 0)
    bus.add_passengers(entering_passengers)


def main() -> None:
    # Create a new bus object for this route.
    bus = Bus(35, 0, 0, 0)

    # Get number of stops and route number
    print("\n\n--------------------------")
    route_number = get_int_input("Enter your route number: ", 0)
    bus_stops = get_int_input("Enter the number of bus stops: ", 3)

    # Loop through stops
    for i in range(1, bus_stops):
        txt = "----- Bus Stop {} ({}/{}) -----"
        print(txt.format(i, bus.get_passengers(), bus.get_capacity()))
        request_exiting_passengers(bus)
        request_passengers_entering(bus)

    # Final bus stop requires different structure
    print("----- Bus Stop " + str(bus_stops) + " (Final stop) -----")
    print("(AUTO) Passengers that exited: " + str(bus.get_passengers()))
    passengers = 0

    # Final output
    txt = "\n----- Route Number: {}. Number of stops: {} -----"
    print(txt.format(route_number, bus_stops))
    print("Happy passengers: " + str(bus.get_happy_passengers()))
    print("Unhappy passengers: " + str(bus.get_unhappy_passengers()))
    print("Ratio of unhappy to happy customers: " + str(bus.get_happy_passenger_ratio()))


while running:
    main()

    # Ask if user wants to add another route
    print("\n\n")
    running = get_bool_input("Would you like to add another route? (Y/N): ")
