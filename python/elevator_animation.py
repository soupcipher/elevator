import sys
import time

def elevator_animation(floors_to_visit):
    SINGLE_FLOOR_TRAVEL_TIME = 10
    total_floors_traveled = 0
    floors_visited = ""
    
    for i in range(len(floors_to_visit)):
        print_open()
        print_load(floors_to_visit[i])

        # If there is another floor to travel to
        if i != len(floors_to_visit) - 1:
            print_closing()
            # Find the difference with next value
            floor_diff = floors_to_visit[i] - floors_to_visit[i+1]

           # Determine if next floor is down or up
            going_up = False
            if floor_diff < 0:
                going_up = True
            
            # Get absolute value    
            total_floors_traveled += abs(floor_diff)

            # Print moving elevator with direction arrow
            for _ in range(abs(floor_diff)):
                print_moving(going_up) 

        if floors_visited:
            # Verify there was a floor change before adding to floors visited
            if floors_to_visit[i] != floors_to_visit[i-1]: 
                floors_visited += ", {0}".format(floors_to_visit[i])
                
        # First floor
        else:
            # Add floor to floors_visited string
            floors_visited += str(floors_to_visit[i])

    travel_time = SINGLE_FLOOR_TRAVEL_TIME * total_floors_traveled
    return "{0} {1}".format(travel_time, floors_visited)

def print_open():
    time.sleep(.2)
    print("____________________________")
    print("| DOORS OPENING            |")
    print("____________________________")
    print("|    |                |    |")
    print("|    |                |    |")
    print("|    |                |    |")
    print("|    |                |    |")
    print("|    |                |    |")
    print("|    |                |    |")
    print("|    |                |    |")
    print("|    |                |    |")
    print("|    |                |    |")
    print("|    |                |    |")
    print("____________________________")
    time.sleep(.5)
    return

# https://ascii.co.uk/art/stickman
def print_load(floor):
    print("____________________________")
    print("| FLOOR {0}                 |".format(floor))
    print("____________________________")
    print("|    |                |    |")
    print("|    |                |    |")
    print("|    |   _\|/^        |    |")
    print("|    |    (_oo /      |    |")
    print("|    |   /-|--/       |    |")
    print("|    |   \ |          |    |")
    print("|    |     /--i       |    |")
    print("|    |    /   L       |    |")
    print("|    |   L            |    |")
    print("|    |                |    |")
    print("____________________________")
    time.sleep(1.5)
    return

def print_closing():
    time.sleep(.2)
    print("____________________________")
    print("| DOORS CLOSING            |")
    print("____________________________")
    print("|         |      |         |")
    print("|         |      |         |")
    print("|         |      |         |")
    print("|         |      |         |")
    print("|         |      |         |")
    print("|         |      |         |")
    print("|         |      |         |")
    print("|         |      |         |")
    print("|         |      |         |")
    print("|         |      |         |")
    print("____________________________")
    time.sleep(1)
    return

def print_moving(going_up):
    char = 'v'
    if going_up:
        char = '^'
        
    print("____________________________")
    print("|            {0}            |".format(char))
    print("____________________________")
    print("|            |             |")
    print("|            |             |")
    print("|            |             |")
    print("|            |             |")
    print("|            |             |")
    print("|            |             |")
    print("|            |             |")
    print("|            |             |")
    print("|            |             |")
    print("|            |             |")
    print("____________________________")
    return

def main():
    if len(sys.argv) <= 1:
        print("ERROR: Please specify a list of floors to visit starting with the current floor. EX: python3 elevator.py 12 2 9 1 32")
        sys.exit(1)

    floors_to_visit = []

    try:
        floors_to_visit = [int(floor) for floor in sys.argv[1:]]
    except ValueError as e:
        print("ERROR: Failed to convert given input to ints. Input: {0} Exeption: {1}".format(sys.argv, e))
        sys.exit(1)
    
    try:
        res = elevator_animation(floors_to_visit)
    except Exception as e:
        print("ERROR: Failed to run elevator on given input: {0} Exeption: {1}".format(floors_to_visit, e))
        sys.exit(1)

    # Split result by first occurance of space
    split = res.split(' ', 1)
    print("Total travel time: {0}".format(split[0]))
    print("Floors visited in order: {0}".format(split[1]))
    sys.exit()

if __name__ == "__main__":
    main()