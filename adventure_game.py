import random
from time import sleep


def print_pause(message):
    print(message)
    sleep(.2)  # Add a delay of 1 second between messages


def start_messages():
    print_pause(
        "You find yourself standing in an open field,"
        " filled with grass, and yellow wildflowers.")
    print_pause(
        "Rumor has it that a wicked fairy is somewhere around here,"
        " and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause(
        "In your hand you hold your trusty (but not very effective),"
        " magic wand.")
    print_pause(f"Your score is: 0")


def get_valid_input():
    choice = input("(Please Enter 1 or 2): ").strip()
    while choice not in ["1", "2"]:
        print_pause("Invalid input. Please try again.")
        choice = input("(Please Enter 1 or 2): ").strip()
    print("")
    return choice


def field(the_enemy, the_wand, score):
    # Things that happen when the player runs back to the field
    print_pause("\nEnter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")

    choice = get_valid_input()
    if choice == "1":
        house(the_enemy, the_wand, score)
    elif choice == "2":
        cave(the_enemy, the_wand, score)


def house(the_enemy, the_wand, score):
    # Things that happen to the player in the house
    new_score = score + 10
    print_pause("Congrats! You have earned 10 points :)")
    print_pause(f"Your score is: {new_score}")
    print_pause("...")
    print_pause("You approach the door of the house.")
    print_pause(
        f"You are about to knock when the door opens"
        f" and out steps a {the_enemy}.")
    print_pause(f"Eep! This is the {the_enemy}'s house!")
    print_pause(f"The {the_enemy} finds you!")

    if not the_wand == 'Wand of Ogoroth':
        print_pause(
            "You feel a bit under-prepared for this,"
            " what with only having a tiny, rusty old magic wand.")

    defend(the_enemy, the_wand, new_score)


def defend(the_enemy, the_wand, score):
    # Things that happen when the player is approached by an enemy
    new_score = score
    print_pause("\nWould you like to (1) cast a spell or (2) run away?")
    choice = get_valid_input()

    if choice == "1":
        if the_wand == "Wand of Ogoroth":
            new_score += 100
            print_pause(
                f"As the {the_enemy} moves to cast a spell,"
                " you raise your new Wand of Ogoroth.")
            print_pause(
                "The Wand of Ogoroth shines brightly in your hand"
                " as you brace yourself for the spell.")
            print_pause(
                f"But the {the_enemy} takes one "
                "look at your shiny new wand and runs away!")
            print_pause(
                f"You have rid the town of the {the_enemy}.")
            print_pause(
                "Congrats! You have earned 100 points, You are amazing! :)")
            print_pause(f"\nYour score is: {new_score}\n")
            print("#" * 100)
            print_pause("  You are victorious!  ".center(100, "#"))
            print("#" * 100)
            return
        else:
            new_score -= 10
            print_pause("You do your best...")
            print_pause(
                "but your rusty old magic wand is no match for the pirate.")
            print_pause("You have been turned into a frog!")
            print_pause("Unfortunately, you lost your last 10 points :(")
            print_pause(f"\nYour score is: {new_score}\n")
            print("#" * 100)
            print_pause("  GAME OVER  ".center(100, "#"))
            print("#" * 100)
            return

    elif choice == "2":
        new_score -= 10
        print_pause("Unfortunately, you lost 10 points :(")
        print_pause(f"Your score is: {new_score}")
        print_pause("...")
        print_pause(
            "You run back into the field. Luckily,"
            " you don't seem to have been followed.")

        field(the_enemy, the_wand, new_score)


def cave(the_enemy, the_wand, score):
    # Things that happen to the player goes in the cave
    if not the_wand == "Wand of Ogoroth":
        new_wand = "Wand of Ogoroth"
        new_score = score + 10
        print_pause("Congrats! You have earned 10 points :)")
        print_pause(f"Your score is: {new_score}")
        print_pause("...")
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Wand of Ogoroth!")
        print_pause(
            "You discard your rusty old magic wand and take the Wand of Ogoroth with you.")
        print_pause("You walk back out to the field.")
        field(the_enemy, new_wand, new_score)
    else:
        print_pause("The cave is empty!")
        print_pause("You already took the Wand of Ogoroth")
        print_pause("You walk back out to the field.")
        field(the_enemy, the_wand, score)


def main():
    enemies = ['Gorgon', 'Dragon', 'Troll', 'Pirate', 'Lion', ]
    the_enemy = random.choice(enemies)
    the_wand = "old magic wand"
    score = 0

    start_messages()
    field(the_enemy, the_wand, score)

    # Playing again
    while True:
        play_again = input("Would you like to play again? (y/n): ").lower()
        if play_again == "yes" or play_again == "y":
            main()
        elif play_again == "no" or play_again == "n":
            print_pause("Thank you for playing!")
            break


main()
