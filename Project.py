def clean_room(floor, room_number, elevator_position):
    # Calculate the actual room number considering the elevator
    actual_room_number = room_number if room_number < elevator_position else room_number + 1

    # Check if the room number is valid
    if actual_room_number >= len(floor):
        print(f"Room {actual_room_number + 1} is not a valid room on this floor.")
        return 0  # Return 0 cleaning time for an invalid room

    occupants = floor[actual_room_number]  # Number of people in the room
    if occupants == 0:
        print(f"Room {actual_room_number + 1} is empty. No cleaning needed.")
        return 0  # Return 0 cleaning time for an empty room
    else:
        cleaning_time = 20 + (2 * occupants)  # Calculate cleaning time
        print(f"Cleaning Room {actual_room_number + 1} (Occupants: {occupants}) on this floor. Cleaning time: {cleaning_time} minutes.")
        return cleaning_time  # Return the cleaning time for the room


def clean_floor(hotel, floor_number, elevator_position):
    print(f"\nCleaning floor {floor_number}:")
    total_cleaning_time = 0  # Total cleaning time for this floor

    # If cleaning a floor other than the 0th floor, add elevator travel time
    if floor_number > 0:
        print("Taking the elevator...")
        total_cleaning_time += 120  # Add elevator travel time (2 minutes)

    # If cleaning the 2nd floor or higher, start walking from the elevator
    if floor_number >= 2:
        print("Starting to walk from the elevator...")
        total_cleaning_time += 10 * elevator_position  # Walking time from elevator

    # Iterate through each room on the floor
    for room_number in range(len(hotel[floor_number])):
        room_cleaning_time = clean_room(hotel[floor_number], room_number, elevator_position)
        total_cleaning_time += room_cleaning_time * 60  # Add cleaning time in seconds
        # Add walking time (10 seconds) between rooms
        total_cleaning_time += 10 * abs(room_number - elevator_position)

    # Calculate the time to walk back to the elevator after cleaning the floor
    walk_to_elevator_time = 10 * abs(room_number - elevator_position)
    print(f"Time to walk back to the elevator: {walk_to_elevator_time} seconds")

    # Update the elevator position to move to the next floor
    if floor_number < len(hotel) - 1:
        elevator_position = len(hotel[floor_number + 1]) // 2

    # Add the time to walk back to the elevator before proceeding to the next floor
    total_cleaning_time += walk_to_elevator_time

    return total_cleaning_time, elevator_position
 

def clean_hotel(hotel):
    total_cleaning_time = 0  # Total cleaning time across all floors
    elevator_position = len(hotel[0]) // 2  # Initial elevator position on the first floor

    # Iterate through each floor of the hotel
    for floor_number in range(len(hotel)):
        # Clean the current floor and get the time to walk back to the elevator
        floor_cleaning_time, elevator_position = clean_floor(hotel, floor_number, elevator_position)
        total_cleaning_time += floor_cleaning_time

    # Convert total cleaning time to hours, minutes, and seconds
    hours, remainder = divmod(total_cleaning_time, 3600)
    minutes, seconds = divmod(remainder, 60)

    print(f"\nTotal cleaning time for the entire hotel: {hours} hours, {minutes} minutes, {seconds} seconds")


# Example hotel with 3 floors and 5 rooms on each floor
hotel = [[2, 3, 'E', 5, 0],
         [4, 3, 'E', 2, 1],
         [0, 5, 'E', 1, 0]]

# Clean the hotel
clean_hotel(hotel)
