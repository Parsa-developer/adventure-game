import time

words = {
    "village": {
        "description": (
            "You stand in a quiet village square. The sun is setting, casting a warm glow over the cobblestone path.\n"
            "To the north, a dark forest looms. To the east, a narrow bridge crosses a river. To the west, an old tavern glows with light."
        ),
        "choices":{
            "north": "forest",
            "east": "bridge",
            "west": "tavern"
        }
    },
    "forest": {
        "description": (
            "You enter a dense, eerie forest. Shadows dance between the trees, and you hear faint whispers.\n"
            "A rusty sword lies in a clearing to the north. To the south, you can return to the village."
        ),
        "choices": {
            "north": "sword",
            "south": "village"
        }
    },
    "sword": {
        "description": (
            "You find a rusty sword half-buried in the dirt. It looks old but sturdy.\n"
            "As you pick it up, a shadowy figure appears and demands a duel! Will you fight or flee?\n"
            "Type 'fight' to battle or 'south' to flee back to the forest."
        ),
        "choices": {
            "fight": "fight",
            "south": "forest"
        }
    },
    "fight": {
        "description": (
            "You draw the rusty sword and face the shadowy figure. With a lucky swing, you defeat it!\n"
            "The figure vanishes, leaving behind a golden amulet. You win!\n"
            "Type 'exit' to end the game."
        ),
        "choices": {
            "exit": "end"
        }
    },
    "bridge": {
        "description": (
            "You stand on a creaky wooden bridge over a rushing river. The water below looks dangerous.\n"
            "To the east, a cave opening beckons. To the west, you can return to the village."
        ),
        "choices": {
            "east": "cave",
            "west": "village"
        }
    },
    "cave": {
        "description": (
            "Inside the dark cave, you see glowing crystals embedded in the walls.\n"
            "A treasure chest sits in the corner, but it’s locked. Without a key, you can’t open it.\n"
            "Type 'west' to return to the bridge."
        ),
        "choices": {
            "west": "bridge"
        }
    },
    "tavern": {
        "description": (
            "The tavern is warm and lively, filled with laughter and the smell of ale.\n"
            "An old bard offers you a mysterious key for a song. You don’t know any songs, so you decline.\n"
            "Type 'east' to return to the village."
        ),
        "choices": {
            "east": "village"
        }
    }
}

def display_room(room):
    print("\n" + "=" * 50)
    print(words[room]["description"])
    print("Available actions:", ", ".join(words[room]["choices"].keys()))
    print("=" * 50)
    time.sleep(1)

def get_player_choice(room):
    valid_choices = words[room]["choices"].keys()
    while True:
        choice = input("\nWhat do you do? ").lower().strip()
        if choice in valid_choices:
            return choice
        print(f"Invalid choice! Please choose: {', '.join(valid_choices)}")

def play_game():
    print("Welcome to the Adventure Game! 🗺️")
    print("Explore the world, make choices, and uncover treasures. Type 'exit' to quit at any time.\n")

    current_room = "village"

    while current_room != "end":
        display_room(current_room)
        choice = get_player_choice(current_room)

        if choice == "exit":
            print("Thanks for playing! Farewell, adventurer! 😊")
            break

        current_room = words[current_room]["choices"][choice]
    
    if current_room == "end":
        print("\nCongratulations! You've completed the adventure! 🎉")

def main():
    while True:
        play_game()
        play_again = input("would you like to play again? (yes/no): ").lower().strip()
        if play_again != "yes" or play_again != "y":
            print("Goodbye, brave adventure! 🗡️")
            break

if __name__ == "__main__":
    main()