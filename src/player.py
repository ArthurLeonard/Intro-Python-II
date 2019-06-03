# Write a class to hold player information, e.g. what room they are in
# currently.



class Player:
	def __init__(self, name, starting_room):
		self.name = name
		self.current_room = starting_room
		self.item_list = ['sword', 'bread', 'lamp']

	def move(self, direction):
		next_room = self.current_room.move_to(direction)
		if next_room is not None:
			self.current_room = next_room
			print(f"\nIn {self.current_room.name}\n\n {self.current_room.description}\n\n")
		else:
			print("There is no room in that direction")

	def get_item(self, item):
		if item not in self.item_list:
			self.item_list.append(item)
		else:
			print(f"You already have a {item}. Drop the {item} you have first if you want to pick up this one.. you greedy pig!")

	def drop_item(self, item):
		if item in self.item_list:
			self.item_list.remove(item)
		else:
			print(f"You are not carrying a {item}")



