# Write a class to hold player information, e.g. what room they are in
# currently.
# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
	def __init__(self, name, starting_room):
		self.name = name
		self.current_room = starting_room

	def move(self, direction):
		next_room = self.current_room.move_to(direction)
		if next_room is not None:
			self.current_room = next_room
			print(f"\nIn {self.current_room.name}\n\n {self.current_room.description}\n\n")
		else:
			print("There is no room in that direction")
