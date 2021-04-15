# Dice Roll Simulator
import random

loop = True
while loop:
    # Provide Menu
    print("\nDice Roll Simulator Menu")
    print("1. Roll Dice Once")
    print("2. Roll Dice 5 Times")
    print("3. Roll Dice 'n' Times")
    print("4. Roll Dice until Snake Eyes")
    print("5. Exit")

    # Display User's Menu Selection
    selection = input("Select an option from the menu (1-5):")

    # Process Menu Selection
    if (selection == "1"):
        print("Roll Dice Once...")
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        total = dice1 + dice2
        print( str(dice1) + "-" + str(dice2) + "(total = " + str(total) + ")")
    
    elif (selection == "2"):
        print("Roll Dice 5 Times...")
        roll_loop = True
        roll_counter = 0
        while roll_loop:
            roll_counter += 1
            dice1 = random.randint(1,6)
            dice2 = random.randint(1,6)
            total = dice1 + dice2
            print( str(dice1) + "-" + str(dice2) + "(total = " + str(total) + ")")
            if (roll_counter >= 5):
                roll_loop = False
    
    elif (selection == "3"):
        roll_times = input("How many times would you like to roll the dice?")
        roll_loop = True
        roll_counter = 0
        while roll_loop:
            roll_counter += 1 
            dice1 = random.randint(1,6)
            dice2 = random.randint(1,6)
            total = dice1 + dice2
            print( str(dice1) + "-" + str(dice2) + "(total = " + str(total) + ")")
            if (roll_counter == int(roll_times)):
                roll_loop = False

    elif (selection == "4"):
        print("Roll Dice Until Snake Eyes...")
        roll_loop = True
        roll_counter = 0
        while roll_loop:
            roll_counter += 1
            dice1 = random.randint(1,6)
            dice2 = random.randint(1,6)
            total = dice1 + dice2
            print( str(dice1) + "-" + str(dice2) + "(total = " + str(total) + ")")
            if (dice1 == 1 and dice2 == 1):
                roll_loop = False
                print("It took " + str(roll_counter) + " rolls to get snake eyes.")
    
    elif (selection == "5"):
        loop = False
    
    print("End Program.")