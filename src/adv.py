from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player1 = Player("tommy", room["outside"])
print(player1.current_room.name, player1.name)

sword = Item('sword', 'A deadly weapon')
print(f"__{sword.name}__:  {sword.description}")
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while True:
	cmd = input('where to?  ')
	if cmd in ['n', 'e', 's', 'w']:
		player1.move(cmd)
	elif cmd == 'q':
		break
	elif cmd == 'd':
		print(f"{player1.current_room.name} has the following items {player1.current_room.item_list}")
	elif cmd == 'i':
		print(f"You the following items {player1.item_list}")
	elif ('get' in cmd or 'take' in cmd):
		item = cmd.split(" ")[1]
		print(f"{item}")
		player1.current_room.remove_item(item)
		player1.get_item(item)

	elif 'drop' in cmd:
		print(f"{cmd}")
		item = cmd.split(" ")[1]
		player1.current_room.add_item(item)
		player1.drop_item(item)
	else:
		print('Valid choices are n, e, s, w for moving in a direction, \td for displaying items in the room. \t i for displaying what you are carrying \t get (item) or drop (item) to access items in the room \t or q to end the game\n') 

