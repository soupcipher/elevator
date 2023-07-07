def elevator(floors_to_visit):
    SINGLE_FLOOR_TRAVEL_TIME = 10
    total_floors_traveled = 0
    floors_visited = ""

    for i in range(len(floors_to_visit)):
        # If there is another floor to travel to
        if i != len(floors_to_visit) - 1:
            # Find the absolute difference with next value
            total_floors_traveled += abs(floors_to_visit[i] - floors_to_visit[i+1])

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

def main():
    return

if __name__ == "__main__":
    main()