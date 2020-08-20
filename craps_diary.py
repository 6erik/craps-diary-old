from roll import Roll

# function to get valid roll values
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
            

session_over = 0
round_number = 0

while (session_over == 0):

    round_number += 1
    round_over = 0
    roll_number = 0
    point = 0
    
    user_input = input("Record a round? ('N' to exit) ").upper()
    
    if (user_input == 'N'):
        session_over = 1
        print("Exiting...")
    
    while (round_over == 0 and session_over == 0):
    
        roll_number += 1
        
        print("\nRound ", round_number, " - Roll ", roll_number, " - Point ", point, sep='')
       
        die1 = ask_roll(1)
        die2 = ask_roll(2)
        
        roll = Roll(die1, die2)
        dice_total = roll.get_dice_total();
        
        print(dice_total)
        
        # if comeout roll
        if (roll_number == 1):
            # if craps -- don't pass win
            if (dice_total == 2 or dice_total == 3):
                round_over = 1
                print("Result: Craps")
                
            # if craps -- don't pass push
            elif (dice_total == 12):
                round_over = 1
                print("Result: Craps")
                
            # if natural -- pass win
            elif (dice_total == 7 or dice_total == 11):
                round_over = 1
                print("Result: Natural")
                
            # else point is established    
            else:
                point = dice_total
        
        # else after first roll
        else:
            # if point -- pass win
            if (dice_total == point):
                round_over = 1
                print("Result: Point")
                
            # if 7 -- don't pass win
            elif (dice_total == 7):
                round_over = 1
                print("Result: 7 Out")
    
    