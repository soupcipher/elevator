#!/bin/bash

SINGLE_FLOOR_TRAVEL_TIME=10

elevator() {
    floors_to_visit=("$@")
    total_floors_traveled=0
    floors_visited=""

    # Get the length of the array
    length_floor_arr=${#floors_to_visit[@]}
    last_index=$((length_floor_arr - 1))

    for ((i=0; i<=$last_index; i++)); do
        # If there is another floor to travel to
        if [ $i != $last_index ]; then
            diff_floors=$((${floors_to_visit[i+1]} - ${floors_to_visit[i]}))
            # Get absolute value
            abs_diff=${diff_floors#-}
            total_floors_traveled=$(($abs_diff + $total_floors_traveled))
        fi

        if [ -n "$floors_visited" ]
        then
            # Verify there was a floor change before adding to floors visited
            if [ ${floors_to_visit[i]} != ${floors_to_visit[i-1]} ]; then
                floors_visited+=", "
                floors_visited+="${floors_to_visit[i]}"
            fi

        else
            floors_visited+="${floors_to_visit[i]}"
        fi
    done

    travel_time=$((SINGLE_FLOOR_TRAVEL_TIME * total_floors_traveled))

    echo -e "\nTotal travel time: $travel_time"
    echo -e "Floors visited in order: $floors_visited"
}

# Example Cases
# ------------------------------------------
# Expected Output:
# Total travel time: 560
# Floors visited in order = 12, 2, 9, 1, 32
floors=(12 2 9 1 32)
elevator ${floors[@]}

# Expected Output:
# Total travel time: 0
# Floors visited in order = 12
floors=(12)
elevator ${floors[@]}

# Expected Output:
# Total travel time: 0
# Floors visited in order = 
floors=()
elevator ${floors[@]}

# Expected Output:
# Total travel time: 0
# Floors visited in order = 3
floors=(3 3 3 3 3)
elevator ${floors[@]}

# Expected Output:
# Total travel time: 19780
# Floors visited in order = -989, -500, 0, 500, 989
floors=(-989 -500 0 500 989)
elevator ${floors[@]}