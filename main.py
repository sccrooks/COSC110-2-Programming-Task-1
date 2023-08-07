route_number = -1
bus_stops = -1
bus_capacity = 35
passengers = 0
happy_passengers = 0
unhappy_passengers = 0


def get_int_input(message, min_input):
    input_num = -1

    while input_num < min_input:
        try:
            input_num = int(input(message))

            if input_num < min_input:
                raise ValueError
            else:
                return input_num
        except:
            print("Invalid input. Please enter an integer of at least " + str(min_input) + ".")


def passengers_exiting():
    global passengers

    if passengers > 0:
        # Do while passengers_exiting > passengers
        x = True
        while x:
            number_passengers_exiting = get_int_input("Enter number of passengers that exited: ", 0)

            if number_passengers_exiting > passengers:
                print("There are not that many passengers on the bus! Please try again.")
                x = True
            else:
                print("Passengers exiting: " + str(number_passengers_exiting))
                passengers -= number_passengers_exiting
                x = False
    else:
        print("(AUTO) Passengers exiting: 0")


def passengers_entering():
    number_passengers = get_int_input("\nEnter number of passengers at stop: ", 0)

    global bus_capacity
    global passengers
    global unhappy_passengers
    global happy_passengers

    remaining_capacity = bus_capacity - passengers

    if number_passengers > remaining_capacity:
        passengers += remaining_capacity
        happy_passengers += remaining_capacity

        number_passengers -= remaining_capacity
        unhappy_passengers += number_passengers
    else:
        passengers += number_passengers
        happy_passengers += number_passengers


while True:
    # Reset data
    happy_passengers = 0
    unhappy_passengers = 0
    passengers = 0

    route_number = get_int_input("Enter your route number: ", 0)
    bus_stops = get_int_input("Enter the number of bus stops: ", 3)

    for i in range(1, bus_stops):
        txt = "----- Bus Stop {} ({}/{}) -----"
        print(txt.format(i, passengers, bus_capacity))
        passengers_exiting()
        passengers_entering()

    print("----- Bus Stop " + str(bus_stops) + " (Final stop) -----")
    print("(AUTO) Passengers that exited: " + str(passengers))
    passengers = 0

    txt = "\n----- Route Number: {}. Number of stops: {} -----"
    print(txt.format(route_number, bus_stops))
    print("Number of happy passengers: " + str(happy_passengers))
    print("Number of unhappy passengers: " + str(unhappy_passengers))

    ratio = unhappy_passengers / happy_passengers if unhappy_passengers > 0 else 0
    print("Ratio of unhappy to happy customers: " + str(ratio))

