from collections import deque
import time
class Room:
    def __init__(self, room_info_list):
        self.room_number = room_info_list[0]
        self.air_speed = room_info_list[1]
        self.power = self.calculate_power()
        self.allocated = False  # Flag to track if the room has been allocated power

    def calculate_power(self):
        if self.air_speed == 'low':
            return 100
        elif self.air_speed == 'medium':
            return 200
        elif self.air_speed == 'high':
            return 300
        else:
            raise ValueError(f"Invalid air speed: {self.air_speed}")

    @classmethod
    def add_rooms(cls, rooms_info_list):
        rooms = []
        for room_info in rooms_info_list:
            rooms.append(cls(room_info))
        return rooms


def schedule_air_conditioning(room_info_list, total_power):
    num_rooms = len(room_info_list)

    # Create a dictionary to group rooms by air_speed
    room_groups = {'low': deque(), 'medium': deque(), 'high': deque()}
    for room_info in room_info_list:
        room = Room(room_info)
        room_groups[room.air_speed].append(room)

    room_queue = deque()
    power_allocated = 0

    while any(not room.allocated for room_group in room_groups.values() for room in room_group):
        for air_speed in ('high', 'medium', 'low'):
            current_room_group = room_groups[air_speed]
            if current_room_group:
                current_room = current_room_group[0]

                if not current_room.allocated and power_allocated + current_room.power <= total_power:
                    # Allocate power to the current room if it hasn't been allocated yet
                    print(f"Allocating {current_room.power} power to room {current_room.room_number} with air speed {current_room.air_speed}")
                    power_allocated += current_room.power
                    current_room.allocated = True
                    room_queue.append(current_room)
                else:
                    # Move the room to the end of the queue for this air_speed group
                    current_room_group.append(current_room_group.popleft())

        # Insufficient power or room already allocated, wait and release power allocated to rooms with the same power
        wait_time = 5  # Adjust the wait time as needed
        print(f"Not enough power or room already allocated. Waiting for {wait_time} seconds...")
        time.sleep(wait_time)

        # Release power allocated to rooms with the same power
        for air_speed in ('high', 'medium', 'low'):
            current_room_group = room_groups[air_speed]
            if current_room_group:
                power_to_release = current_room_group[0].power
                while current_room_group and current_room_group[0].allocated and current_room_group[0].power == power_to_release:
                    released_room = current_room_group.popleft()
                    power_allocated -= released_room.power


# room_info_list = [[106, 'low'], [107, 'medium'], [120, 'low'], [230, 'high']]
# rooms = Room.add_rooms(room_info_list)
# total_power = 600
# schedule_air_conditioning(room_info_list, total_power)