robot_name = input("Robot Name: ")
patrol_cycles = int(input("How many patrol cycles? "))

counter = 1

print()

while counter <= patrol_cycles:
    print(robot_name, "Patrol Cycle", counter, "Complete")
    counter += 1

print("\nMission Completed")
