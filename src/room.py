# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item 
from items import items


class Room:
	def __init__ (self, name, description):
		self.name = name
		self.description = description
		self.n_to = None
		self.e_to = None
		self.s_to = None
		self.w_to = None
		self.item_list = [items['gold'], items['wine']]

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
		for thing in self.item_list:
			if thing.name == item.name:
				self.item_list.remove(thing)
				item.on_take()
				return 1
		# if item in self.item_list:
		# 	self.item_list.remove(item)
		print(f"{self.name} does not contain {item.name}\n\n")
		return 0

	def add_item (self, item):
		for thing in self.item_list:
			if thing.name == item.name:
				print(f"{self.name} already has {item.name}")
				return 0
		self.item_list.append(item)
		item.on_drop()
		return 1

		# if item not in self.item_list:
		# 	self.item_list.append(item)
		# else: 
		# 	print(f"{item} already exists in {self.name}\n\n")
