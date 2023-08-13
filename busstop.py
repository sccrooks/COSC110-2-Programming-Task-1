#
#   Author: Scott Crooks
#
#   Purpose: System for tracking the number of happy/unhappy passengers
#            for Codetown school bus stops/routes
#
#   Usage: To use, run this file
#

class Bus:
    def __init__(self, capacity: int = 35, passengers: int = 0,
                 happy_passengers: int = 0, unhappy_passengers: int = 0):
        self._capacity = capacity
        self._passengers = passengers
        self._happy_passengers = happy_passengers
        self._unhappy_passengers = unhappy_passengers

    def get_happy_passenger_ratio(self) -> float:
        """
        get_happy_passenger_ratio returns the ratio of unhappy to happy
        passengers calculated as: _happy_passengers / _unhappy_passengers

        :return: float
        """
        # If there are no unhappy passengers return 0.
        # Otherwise, return unhappy_passengers / happy_passengers
        return round(self._happy_passengers / self._unhappy_passengers, 2) if self._unhappy_passengers > 0 else 0

    def get_capacity(self) -> int:
        """
        get_capacity returns the capacity of this bus.

        :return: int
        """
        return self._capacity

    def get_passengers(self) -> int:
        """
        get_passengers returns the number of passengers in this bus.

        :return: int
        """
        return self._passengers

    def add_passengers(self, passengers: int) -> None:
        """
        add_passengers calculates the number of passengers able to fit into
        the bus and

        :param passengers:
        """
        # Guard clause, there is no need to continue if passengers are <= 0
        if passengers <= 0:
            return

        # Calculate the overfilled amount, I.e. the number of passengers unable
        # to enter the bus due to capacity limitations.
        if passengers + self._passengers < self._capacity:
            overfill = 0
        else:
            overfill = passengers + self._passengers - self._capacity

        self._passengers += passengers - overfill
        self._happy_passengers += passengers - overfill
        self._unhappy_passengers += overfill

    def set_passengers(self, passengers: int) -> None:
        """
        set_passengers sets the local variable _passengers to the inputted value passengers.

        WARNING: This function does not contain protections for preventing going over _capacity or going under 0.
                 Use bus.add_passengers to prevent this.

        :param passengers: New Value
        """
        self._passengers = passengers

    def get_happy_passengers(self) -> int:
        """
        get_happy_passengers returns the number of happy customers

        :return: int
        """
        return self._happy_passengers

    def get_unhappy_passengers(self) -> int:
        """
        get_unhappy_passengers returns the number of unhappy customers

        :return: int
        """
        return self._unhappy_passengers


def request_int_input(message: str, minimum: int = None, maximum: int = None) -> int:
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


def request_bool_input(message: str) -> bool:
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


def request_passengers_exiting(bus: Bus) -> None:
    """
    request_exiting_passengers requests an integer input from the user
    specifying the amount of passengers exiting the bus.

    :param bus: The bus object this function will perform on.
    """
    if bus.get_passengers() > 0:
        passengers_exiting = request_int_input("Enter number of passengers that exited: ", 0, bus.get_passengers())
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
    entering_passengers = request_int_input("Enter number of passengers at stop: ", 0)
    bus.add_passengers(entering_passengers)


def main() -> None:
    """
    main contains the functionality for this program's core loop.
    """
    # Create a new bus object for this route.
    bus = Bus()

    # request the  number of stops and route number.
    print("\n\n--------------------------")
    route_number = request_int_input("Enter your route number: ", 0)
    bus_stops = request_int_input("Enter the number of bus stops: ", 3)

    # Loop through bus stops.
    for i in range(1, bus_stops):
        txt = "----- Bus Stop {} ({}/{}) -----"
        print(txt.format(i, bus.get_passengers(), bus.get_capacity()))
        request_passengers_exiting(bus)
        request_passengers_entering(bus)

    # Remaining passengers must exit at final stop.
    print("----- Bus Stop " + str(bus_stops) + " (Final stop) -----")
    print("(AUTO) Passengers that exited: " + str(bus.get_passengers()))

    # Final output.
    txt = "\n----- Route Number: {}. Number of stops: {} -----"
    print(txt.format(route_number, bus_stops))
    print("Happy passengers: " + str(bus.get_happy_passengers()))
    print("Unhappy passengers: " + str(bus.get_unhappy_passengers()))
    print("Ratio of unhappy to happy customers: " + str(bus.get_happy_passenger_ratio()))


while True:
    main()

    # Ask whether user wants to add another route
    print("\n\n")
    if not request_bool_input("Would you like to add another route? (Y/N): "):
        break
