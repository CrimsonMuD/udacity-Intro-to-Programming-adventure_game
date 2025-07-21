import time
import random

villain = ["Zombie", "Vampire", "Werewolf", "Swamp Monster", "Mummy"]
super_weapon = ["Boomstick", "Unwieldy Bloody Axe", "Chainsaw",
                "Ancient Magical Sword"]
weapon = "dagger"
monster_guaranteed_next_spawn = False


def print_pause(message):
    print(message)
    time.sleep(2)


def invalid_response():
    print_pause(
        "I'm sorry, there are no other options. Please respond with 1, or 2."
    )


def valid_input(prompt, options):
    while True:
        option = input(prompt).lower()
        if option in options:
            return option
        print(f'Option {option} is invalid. Try again!')


def ambush():
    global monster_guaranteed_next_spawn

    if monster_guaranteed_next_spawn:
        monster_guaranteed_next_spawn = False
        return True
    else:
        presence = random.choice([True, False])
        return presence


def intro():
    global enemy
    global monster_guaranteed_next_spawn
    global weapon
    monster_guaranteed_next_spawn = False
    enemy = random.choice(villain)
    weapon = "dagger"
    print_pause("-----------------------------------------------------------")
    print_pause("People have gone missing in town")
    print_pause(
        "You decide to investigate where the first disappearance occurred."
    )
    message = f"You heard rumors that a {enemy} may be hiding in the area."
    print_pause(message)
    print_pause("Armed with only a " + weapon + " you enter a grassy field.")
    field()


def field():
    print_pause(
        "Inside the field, you look beyond it and see two different locations."
    )
    response = valid_input(
        "Where would you like to go?\n"
        "1. An old dilapitated house\n"
        "2. A cave looming in the distance\n",
        ['1', '2']
    )
    if response == '1':
        print_pause(
            "You begin to march through the tall grass, towards the "
            "old dilapitated house."
        )
        house()
    elif response == '2':
        print_pause(
            "You begin to march through the tall grass, towards the "
            "cave looming in the distance."
        )
        cave()


def play_again():
    print_pause("Would you like to play again?")
    response = valid_input(
        "1. Yes\n"
        "2. No ",
        ['1', '2']
    )
    if response == '1':
        print_pause("Goodluck!")
        global monster_guaranteed_next_spawn
        monster_guaranteed_next_spawn = False
        intro()
    elif response == '2':
        print_pause("I understand, " + enemy + "s are scary! Run!")
        print_pause(
            "----------------------------------------------------------"
        )


def check_weapon():
    global weapon
    for sw in super_weapon:
        if sw.lower() in weapon.lower():
            return True
    return False


def item_gain():
    global weapon, monster_guaranteed_next_spawn
    new_weapon = random.choice(super_weapon)
    weapon = new_weapon
    print_pause(
        "Just as you were about to leave, out of the corner of your "
        "eye, you spot something. "
    )
    print_pause("You wretch the object out of some muck and debris")
    print_pause("Behold! You found the " + weapon + " !!")
    print_pause(
        "With " + weapon + " in hand, you return to the field, more "
        "confident than ever."
    )
    monster_guaranteed_next_spawn = True
    field()


def victory():
    print_pause("Out of the shadows, jumps " + enemy + " swinging and "
                "gnashing wildly at you!")
    print_pause(
        "You desperately dodge, roll, and weave between it's strikes."
    )
    print_pause("It roars in frustration, as you ready your " + weapon +
                " aiming for the " + enemy + "'s head.")
    print_pause("With one fell strike from your " + weapon + " you destroy "
                "the creature, completely removing it's head!")
    print_pause(
        "Still panting, you feel a great sense of pride and "
        "accomplishment for what you have done."
    )
    print_pause("The monster has been defeated, the town has been saved.")
    play_again()


def failure():
    print_pause("Out of the shadows, jumps " + enemy + " swinging and "
                "gnashing wildly at you!")
    print_pause(
        "You desperately dodge, roll, and weave between it's strikes."
    )
    print_pause("It roars in frustration, as you ready your " + weapon +
                " aiming for the " + enemy + "'s head.")
    print_pause("But your " + weapon + " wasn't enough! It weakly strikes the "
                + enemy + " and falls to the ground")
    print_pause("The " + enemy + " lunges once more, fatally wounding you.")
    print_pause(
        "The " + enemy + " towers above you, as your vision fades to black."
    )
    print_pause(
        "Unfortunately, the creature has won. The townspeople will "
        "continue to dissapear. You have lost the game."
    )
    play_again()


def house():
    print_pause("Before you is the old, dilapitated house.")
    print_pause(
        "Great, dark, and ominous clouds are cast behind it's "
        "sagging, rickety roof."
    )
    print_pause(
        "It's windows cracked, and broken. Shadows dance to and fro, "
        "beckoning you to approach it's creaky front porch."
    )

    monster_present = ambush()

    if monster_present is True:
        if check_weapon() is True:
            print_pause(
                "With " + weapon + " in hand, you approach the door "
                "of the house confidently."
            )
            response = valid_input(
                "Do you....\n1. Knock on the door.\n"
                "2. Go back to the field?\n",
                ['1', '2']
            )
            if response == '1':
                print_pause(
                    "You bang on the door, " + weapon + " poised to strike"
                )
                victory()
            elif response == '2':
                print_pause(
                    "Though you felt ready, you choose to head back "
                    "to the field."
                )
                field()
        else:
            print_pause(
                "With only your little " + weapon + " in hand, you "
                "nervously approach the door of the house."
            )
            response = valid_input(
                "Should you....\n1. Knock on the door.\n"
                "2. Run back to the field?\n",
                ['1', '2']
            )
            if response == '1':
                print_pause("With sweaty palms, you knock on the door.")
                failure()
            elif response == '2':
                print_pause(
                    "You back away from the dilapitated house and "
                    "return to the field."
                )
                field()

    else:
        print_pause(
            "With " + weapon + " in hand, you approach the door of the house."
        )
        response = valid_input(
            "Do you....\n1. Knock on the door.\n"
            "2. Go back to the field?\n",
            ['1', '2']
        )
        if response == '1':
            print_pause(
                "Your hand goes out to knock, as the door slowly "
                "creaks open."
            )
            print_pause(
                "Rats skitter across the floor, running to the shadows, "
                "as you enter the domain."
            )
            print_pause(
                "You search here and there, finding no monster or clues, "
                "you turn to leave."
            )
            if check_weapon() is False:
                item_gain()
            else:
                field()

        elif response == '2':
            print_pause(
                "You back away from the door, and return to the field."
            )
            field()


def cave():
    print_pause(
        "Before you are several rock formations, and the opening to "
        "the large looming cave."
    )
    print_pause(
        "Great stalagtites jut out from the roof and sides of the "
        "cave, forming a wicked smile."
    )
    print_pause(
        "The shadows are deep, and you can hear the 'pit pat' of "
        "dripping water deep within the cave."
    )

    monster_present = ambush()

    if monster_present is True:
        if check_weapon() is True:
            print_pause(
                "With " + weapon + " in hand, you confidently "
                "approach the muddy entrance of the cave."
            )
            response = valid_input(
                "Do you....\n1. Enter the shadows of the cave?\n"
                "2. Go back to the field?\n",
                ['1', '2']
            )
            if response == '1':
                print_pause(
                    "You stomp your way forward, " + weapon +
                    " poised to strike"
                )
                victory()
            elif response == '2':
                print_pause(
                    "Though you felt ready, you choose to head back "
                    "to the field."
                )
                field()
        else:
            print_pause(
                "With only your little " + weapon + " in hand, you "
                "nervously approach the muddy entrance of the cave."
            )
            response = valid_input(
                "Should you....\n1. Enter the shadows of the cave?\n"
                "2. Run back to the field?\n",
                ['1', '2']
            )
            if response == '1':
                print_pause(
                    "With sweaty palms, you timidly step forth into "
                    "the damp and dark cave."
                )
                failure()
            elif response == '2':
                print_pause(
                    "You back away from the muddy entrance and return "
                    "to the field."
                )
                field()

    else:
        print_pause(
            "With " + weapon + " in hand, you approach the muddy "
            "entrance of the cave."
        )
        response = valid_input(
            "Do you....\n1. Enter the shadows of the cave?\n"
            "2. Go back to the field?\n",
            ['1', '2']
        )
        if response == '1':
            print_pause(
                "You step forward into the dark of the cave, boots "
                "sinking in mud."
            )
            print_pause(
                "Bats screech and flap about, blowing past you, out "
                "of the mouth of the cave."
            )
            print_pause(
                "You search here and there, finding no monster or "
                "clues, you turn to leave."
            )
            if check_weapon() is False:
                item_gain()
            else:
                field()

        elif response == '2':
            print_pause("You exit the damp cave, and return to the field.")
            field()


intro()
