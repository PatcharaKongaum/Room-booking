"""Room Booking System"""
rooms = {
    101: "Available",
    102: "Available",
    103: "Available",
    201: "Available",
    202: "Available",
    203: "Available"
}

def display_rooms():
    """Displays the status of all rooms."""
    print("\n--- Room Status ---")
    available_count = 0
    booked_count = 0
    for room, status in rooms.items():
        print(f"Room {room}: {status}")
        if status == "Available":
            available_count += 1
        else:
            booked_count += 1
    print(f"\nTotal Available: {available_count} | Total Booked: {booked_count}")
    print("-------------------")

def book_room():
    """Allows a user to book an available room."""
    print("\n--- Book a Room ---")
    try:
        room_num = int(input("Enter the room number you want to book: "))
    except ValueError:
        print("Invalid input. Please enter a valid room number (e.g., 101).")
        return

    if room_num not in rooms:
        print(f"Room {room_num} does not exist.")
    elif rooms[room_num] != "Available":
        print(f"Room {room_num} is already booked by {rooms[room_num]}.")
    else:
        guest_name = input("Enter your name for the booking: ").strip()
        if guest_name:
            rooms[room_num] = guest_name.title()
            print(f"✅ Success! Room {room_num} is now booked for {rooms[room_num]}.")
        else:
            print("Guest name cannot be empty.")

def check_out():
    """Allows a user to clear a booking (check out)."""
    print("\n--- Check Out/Cancel Booking ---")
    try:
        room_num = int(input("Enter the room number to check out/cancel: "))
    except ValueError:
        print("Invalid input. Please enter a valid room number.")
        return

    if room_num not in rooms:
        print(f"Room {room_num} does not exist.")
    elif rooms[room_num] == "Available":
        print(f"Room {room_num} is already available.")
    else:
        guest = rooms[room_num]
        rooms[room_num] = "Available"
        print(f"✅ Success! Room {room_num} checked out. Thank you, {guest}!")

def main_menu():
    """Displays the main menu and handles user choices."""
    while True:
        print("\n==================================")
        print("    ROOM BOOKING SYSTEM MENU    ")
        print("==================================")
        print("1. Display Available/Booked Rooms")
        print("2. Book a Room")
        print("3. Check Out/Cancel Booking")
        print("4. Exit")
        print("----------------------------------")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            display_rooms()
        elif choice == '2':
            book_room()
        elif choice == '3':
            check_out()
        elif choice == '4':
            print("Exiting the Room Booking System. Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice. Please enter a number between 1 and 4.")

main_menu()
