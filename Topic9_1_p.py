# Topic9_1_p.py
# Practical Programming Question
# Create a Room class for a booking scenario.

class Room:
    """Represents a room available for booking."""

    def __init__(self, room_id, room_type, price):
        self.room_id = room_id
        self.room_type = room_type
        self.price = price

    def __str__(self):
        return f"[{self.room_id}] {self.room_type} - ${self.price:.2f} per night"


# Create one Room object
room1 = Room(12, "Deluxe Room", 150)

# Print the room
print(room1)