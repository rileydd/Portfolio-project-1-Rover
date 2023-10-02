# ENDG 233 Fall 2023
# Portfolio Project 1
# rover.py
# Program for calculating the time it takes a rover to travel depending on rover parameters and storm status.
# RILEY DUNN


# These are the required inputted values and thier respective variables

rover_type = int(input('Which rover would you like to move? '))     # rover_type designates Charlie(1), Alpha(2) and November(3)
total_distance = float(input('How far is the mission in km? '))     # total_distance is the distance of the mission
storm = input('Is there a storm in the forecast (True or False)? ') # string: true for storm false for no storm

 # parameters for Charlie
if rover_type == 1:
    
    battery_life = 100                  # 100 kWh
    solar_capacity = 5                  # 5 kW
    avg_velocity = 5                    # 5 km/hr
    battery_efficiency = 50/100         # 50 kWh / 100km

# parameters for Alpha
elif rover_type == 2:
    
    battery_life = 130                  # 130 kWh
    solar_capacity = 8                  # 8 kW
    avg_velocity = 4                    # 4 km/hr
    battery_efficiency = 40/100         # 40 kWh / 100km

# parameters for November
elif rover_type == 3:
    
    battery_life = 80                   # 80 kWh
    solar_capacity = 4                  # 4 kW
    avg_velocity = 6                    # 6 km/hr
    battery_efficiency = 30/100         # 30 kWh / 100km


# else branch ending the code if the program runs an invalid input
else:
    print('Rover number not recognized.')
    exit()


# calculations to determine the total time 
num_charges = total_distance // (battery_life/ battery_efficiency)              # num_charges is the amount of times the rover has to charge rounded down to the nearest integer

time_charging = battery_life / solar_capacity                                   # time_charging is the amount of time the rover will spend on each charge

time_moving = total_distance / avg_velocity                                     # time_moving is the total time the rover will be moving

total_time = (num_charges * time_charging) + time_moving                        # total_time is the number of charges on the trip multiplied by the time it takes to charge added to the time moving


# results if there is a storm
if storm == 'True':

    total_time = total_time * 1.2


# printing the total time for the designated rover to travel the inputted distance
print("The total travel time for Rover {0} to travel {1:0.1f} km is {2:0.1f} hours.".format(rover_type, total_distance, total_time))







