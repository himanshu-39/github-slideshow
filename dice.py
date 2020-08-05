def dice():

    from random import randint
    roll = randint(1, 100)
    tries = 0
    while tries < 5:
        num = int(input("ENTER A NUMBER: "))
        if num == roll:
            print("You won!")
            break

        elif num < roll:
            print("The number is too low.")

            tries += 1
            print("You have", 5-tries, "tries left." )
            hint = int(input("""Do you want a hint? If yes type '1'(It will deduct a chance!);
                If no type '0': """))
            if hint == 1:
                print("The number lies in the range; ", (roll-2), " to ", (roll+2))
                tries += 1
                print("You have", 5-tries, "tries left." )
            else:
                print("OK! Try harder.")
        elif num > roll:
            print("The number is too high.")
            tries += 1
            print("You have", 5-tries, "tries left." )

            hint = input("""Do you want a hint? If yes type '1'(It will deduct a chance!);
                If no type '0': """)
            if hint == 1:
                print("The number lies in the range; ", (roll-2), " to ", (roll+2))
                tries += 1
                print("You have", 5-tries, "tries left." )
            else:
                print("OK! Try harder.")

    return roll


print("The outcome is",dice())
