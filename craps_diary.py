from roll import Roll
from prettytable import PrettyTable

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

# function to find money won if field was bet every opportunity
def check_field_winnings(session):
    sum = 0
    
    for j in range(len(session)):
    
            round = session[j]
        
            for i in range(len(round)):
                roll = round[i]
                d_total = roll.get_dice_total()
                
                if (d_total == 2):
                    sum += 2
                elif (d_total == 3 or d_total == 4 or d_total == 9 or d_total == 10 or d_total == 11):
                    sum += 1
                elif (d_total == 12):
                    sum += 3
                else:
                    sum -= 1
                    
    print("Field Winnings:", sum)

# function to find money won if hardway bets placed every opportunity
def check_hardway_winnings(session):
    sum = 0
   
    for j in range(len(session)):
    
            round = session[j]
            
            # loop skips comeout roll (index 0)
            for i in range(1, len(round)):
                roll = round[i]
                d_total = roll.get_dice_total()
                
                d_1 = roll.get_die1()
                d_2 = roll.get_die2()

                if (d_1 == d_2):
                    if (d_total == 4 or d_total == 10):
                        sum += 10
                    elif (d_total == 6 or d_total == 8):
                        sum += 8
                else:
                    if (d_total == 7 or d_total == 4 or d_total == 6 or d_total == 8 or d_total == 10):
                        sum -= 1
                    
    print("All Hardway Winnings:", sum)
 
def check_freqs(session):
 
    # array to hold frequency of roll totals (2-12)
    freq_total = [0] * 13
    
    # array to hold frequency of each die (1-6)
    freq_die = [0] * 7
    
    for j in range(len(session)):
        
        round = session[j]
        
        for i in range(0, len(round)):
            roll = round[i]
            d_total = roll.get_dice_total()
            
            d_1 = roll.get_die1()
            d_2 = roll.get_die2()
            
            freq_total[d_total] += 1
            freq_die[d_1] += 1
            freq_die[d_2] += 1
    
    # print freq_total
    print("-- Total frequencies --", end='')
    for i in range(1, 13):
        print(i, ": ", freq_total[i], ", ", sep='', end=' ')
    
    print("\nDie frequencies: ", end='')
    # print freq_die
    for i in range(1, 7):
        print(i, ": ", freq_die[i], ", ", sep='', end=' ')
        
def check_freqs_tables(session):
 
    # array to hold frequency of roll totals (2-12)
    freq_total = [0] * 13
    
    # array to hold frequency of each die (1-6)
    freq_die = [0] * 7
    
    for j in range(len(session)):
        
        round = session[j]
        
        for i in range(0, len(round)):
            roll = round[i]
            d_total = roll.get_dice_total()
            
            d_1 = roll.get_die1()
            d_2 = roll.get_die2()
            
            freq_total[d_total] += 1
            freq_die[d_1] += 1
            freq_die[d_2] += 1
    
    # print freq_total
    print("\n Roll total frequencies: ")
    table_freq_total = PrettyTable(['Total', 'Freq', 'Total2', 'Freq2'])
    table_freq_total.add_row([1, "--", 7, freq_total[7]])
    table_freq_total.add_row([2, freq_total[2], 8, freq_total[8]])
    table_freq_total.add_row([3, freq_total[3], 9, freq_total[9]])
    table_freq_total.add_row([4, freq_total[4], 10, freq_total[10]])
    table_freq_total.add_row([5, freq_total[5], 11, freq_total[11]])
    table_freq_total.add_row([6, freq_total[6], 12, freq_total[12]])
    print(table_freq_total)
    
    # print freq_die
    print("Die frequencies: ")
    table_freq_die = PrettyTable(['Value', 'Freq'])
    table_freq_die.add_row([1, freq_die[1]])
    table_freq_die.add_row([2, freq_die[2]])
    table_freq_die.add_row([3, freq_die[3]])
    table_freq_die.add_row([4, freq_die[4]])
    table_freq_die.add_row([5, freq_die[5]])
    table_freq_die.add_row([6, freq_die[6]])
    print(table_freq_die)
    
session_over = 0
round_number = 0

round_list = []

while (session_over == 0):

    round_number += 1
    round_over = 0
    roll_number = 0
    point = 0
    
    roll_list = []
    
    user_input = input("\nRecord a round? ('N' to exit) ").upper()
    
    if (user_input == 'N'):
        session_over = 1
        # print("Exiting...")
        for j in range(len(round_list)):
            print("-- Round ", j+1, "--", sep='')
            temp_round = round_list[j]
        
            for i in range(len(temp_round)):
                print("Roll ", i+1, ": ", sep='', end='')
                temp_roll = temp_round[i]
                temp_roll.print_dice()
                
        check_field_winnings(round_list)
        check_hardway_winnings(round_list)
        check_freqs_tables(round_list)
        
    while (round_over == 0 and session_over == 0):
    
        roll_number += 1
        
        print("\nRound ", round_number, " - Roll ", roll_number, " - Point ", point, sep='')
       
        # get user input for dice
        die1 = ask_roll(1)
        die2 = ask_roll(2)
        
        # create Roll object with each die
        roll = Roll(die1, die2)
        dice_total = roll.get_dice_total();
        
        # append every roll to a list
        roll_list.append(roll)
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
            
        if (round_over == 1):
            # append each list of rolls to a list
            round_list.append(roll_list)
            
            for i in range(len(roll_list)):
                print("Roll ", i+1, ": ", sep='', end='')
                roll_list[i].print_dice()