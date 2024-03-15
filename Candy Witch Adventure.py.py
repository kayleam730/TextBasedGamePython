def display_instructions():
    print("Welcome to the Candy Witch Adventure! You must navigate between rooms using the directional commands North, South, East, and West. Use the command 'go' before each directional command when prompted and use 'grab' when picking up an item. Collect all the magical items to escape before the Candy Witch catches you. Good luck!")

def display_room(room, items):
    print("You are in the " + room + ".")
    if len(items) > 0:
        print("In this room, you see the following items: ")
        for item in items:
            print("- " + item)
    else:
        print("There are no items in this room.")

def display_inventory(inventory):
    if len(inventory) > 0:
        print("Your inventory contains the following items: ")
        for item in inventory:
            print("- " + item)
    else:
        print("Your inventory is empty.")

def get_input():
    return input("What would you like to do? ").strip().lower()

def play_game():
    rooms = {
        "Living Room": {"North": "Bedroom", "South": "Witch's Spell Room", "East": "Dining Room", "West": "Library"},
        "Witch's Spell Room": {"North": "Living Room", "West": "Pantry", "item": "Axe"},
        "Pantry": {"East": "Living Room", "item": "Your niece"},
        "Bedroom": {"East": "Bathroom", "item": "Gingerbread key", "South": "Living Room"},
        "Bathroom": {"West": "Bedroom", "item": "Sour-smelling cloak"},
        "Dining Room": {"North": "Living Room", "East": "Kitchen", "item": "Poison"},
        "Kitchen": {"VILLAIN": "Candy Witch", "description": "Oh no! The witch saw you! Game over!"},
        "Library": {"East": "Living Room", "item": "Spellbook"}
    }

    inventory = []

    display_instructions()

    current_room = "Living Room"

    while True:
        display_room(current_room, rooms[current_room].get("item", []))
        display_inventory(inventory)

        user_input = get_input()

        if user_input == "quit" or user_input == "goodbye":
            print("Thank you for playing! Goodbye.")
            break
        elif user_input.startswith("go "):
            direction = user_input[3:].strip().capitalize()
            if direction in rooms[current_room]:
                new_room = rooms[current_room][direction]
                print(f"You move {direction} to the {new_room}.")
                current_room = new_room

                # Check if the Candy Witch is in the current room after moving
                if "VILLAIN" in rooms[current_room]:
                    print(rooms[current_room]["description"])
                    print("Thanks for playing. Hope you had fun!!! ")
                    break
            else:
                print("Invalid direction. Try again.")
        elif user_input.startswith("grab "):
            item_name = user_input[5:].strip().capitalize()
            if "item" in rooms[current_room] and item_name == rooms[current_room]["item"]:
                print(f"You grabbed {item_name}.")
                inventory.append(item_name)
                del rooms[current_room]["item"]  # Remove the item from the room after grabbing
            else:
                print("Cannot grab that item here. Try again.")
        else:
            print("Invalid command. Try again.")

        # Check if the player has collected all items
        if all(item in inventory for item in ["Axe", "Your niece", "Gingerbread key", "Sour-smelling cloak", "Poison", "Spellbook"]):
            print("Congratulations! You have collected all items and escaped from the Candy Witch!")
            print("Thanks for playing. Hope you enjoyed it.")
            break

if __name__ == "__main__":
    play_game()
