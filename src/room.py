# Implement a class to hold room information. This should have name and
# description attributes.
# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
	def __init__ (self, name, description):
		self.name = name
		self.description = description
		self.n_to = None
		self.e_to = None
		self.s_to = None
		self.w_to = None
		self.item_list = ['gold', 'wine', 'fire']

	def move_to (self, direction):
		if direction == "n":
			return self.n_to
		elif direction == "e":
			return self.e_to
		elif direction == "s":
			return self.s_to
		elif direction == "w":
			return self.w_to

		else:
			return None

	def remove_item (self, item):
		if item in self.item_list:
			self.item_list.remove(item)
		else: 
			print(f"{self.name} does not contain {item}\n\n")

	def add_item (self, item):
		if item not in self.item_list:
			self.item_list.append(item)
		else: 
			print(f"{item} already exists in {self.name}\n\n")
