from roll import Roll

game_over = 0
roll_number = 0
point = 0

def ask_roll(die_num):
    while True:
        try:
            print("Die #", die_num, ": ", sep='', end='')
            die_value = int(input())
        except ValueError: # if input is not an integer
            print("Invalid value entry.")
            continue
        if (1 <= die_value <= 6):
            return die_value
        else: # if input integer is not in 1-6 range
            print("Invalid value entry.")

while (game_over == 0):
    roll_number += 1
    
    print("\nRoll #", roll_number, sep='')
   
    die1 = ask_roll(1)
    die2 = ask_roll(2)
    
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