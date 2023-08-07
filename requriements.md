The mayor of Codetown thinks that current school times are not aligned to the needs of modern working parents. However, she realises that modifying school hours will have flow-on effects to areas such as public transport. Therefore, before making any changes, she has decided she needs more data to determine how public transport is currently utilised. She has asked you to develop a program that can be used by the town's bus drivers to collect some of this information.

A Codetown city bus can hold 35 passengers. For each route, a bus starts at a particular bus stop and picks up any passengers that are waiting (provided they all fit on the bus - no more passengers are picked up if the bus is full). Until the end of the route, the bus repeatedly moves to the next bus stop, dropping off any passengers that wish to get off the bus at that point and picking up any waiting passengers that can fit on the bus.

The mayor has asked you to develop a Python program that does the following. At the start of the program, the driver should be asked the route number, how many stops there are along that route, and the number of passengers at the start of the route. Then, for each remaining stop, the driver should be prompted to enter the number of passengers leaving the bus, and the number of passengers waiting to get on the bus at that stop (though all passengers must leave and no passengers can get on the bus at the last stop at the end of the route). Your program should then output the route number, the total number of passengers that got on the bus ("happy customers"), the total number of passengers that were unable to get on the bus because it was too full ("unhappy customers"), and the ratio of happy customers to unhappy customers (to two decimal places, and set to 0 if there were no unhappy customers).

Note: Your program should ensure that the route number is a positive integer, there are at least three stops (including the start and end) on the route, and the number of passengers getting on and off the bus at each stop are non-negative integers. You also need to ensure that the number of passengers that want to get off the bus at any stop is not greater than the number of passengers currently on the bus, and that the number of passengers ever on a bus does not exceed the maximum allowed. If any of these conditions are not met, you need to prompt the driver to re-enter the information, as it is likely it was a typing mistake.

# Input
* Input route number
* Input number of stops
* Input number of passengers at the start of the route\
* At each stop ask for the number of passengers leaving and number entering
* All passengers must leave and no passengers are allowed to enter at the end of the route

# Output
* Route number
* The number of passengers that entered (Happy customers)
* The number unable to get on the bus (Unhappy customers)
* Ratio of unhappy to happy customers (2dp) 0 if no unhappy customers

# Musts:
* Bus has 35 slots
* Positive route number
* Minimum 3 stops
* If above is false re-enter information