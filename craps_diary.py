from roll import Roll

game_over = 0
roll_number = 0
point = 0

while (game_over == 0):

    valid_roll = 0
    roll_number += 1
    
    print("\nRoll #", roll_number)
    die1 = int(input("Die 1: "))
    die2 = int(input("Die 2: "))
    
    while (valid_roll == 0): 
        if (die1 >= 1 and die1 <= 6 and die2 >= 1 and die2 <= 6):
            valid_roll = 1
        else:
            print("Invalid roll values -- Try again")
            die1 = int(input("Die 1: "))
            die2 = int(input("Die 2: "))
        
    
    
    roll = Roll(die1, die2)
    dice_total = roll.get_dice_total();
    
    print(dice_total)
    
    if (roll_number == 1):
        if (dice_total == 2 or dice_total == 3):
            game_over = 1
            print("Craps")
            
        elif (dice_total == 12):
            game_over = 1
            print("Craps")
            
        elif (dice_total == 7 or dice_total == 11):
            game_over = 1
            print("Natural")
            
        else:
            point = dice_total
        
    else:
        if (dice_total == point):
            game_over = 1
            print("Point")
        
        elif (dice_total == 7):
            game_over = 1
            print("7 Out")