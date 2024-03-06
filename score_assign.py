from global_vars import *
from prettytable import PrettyTable

#score selection
def score_assign():
    global str_score, dex_score, con_score, int_score, wis_score, cha_score, score_choice, starting_scores
    standard_array = [15, 14, 13, 12, 10, 8]
    plr_scores = [str_score, dex_score, con_score, int_score, wis_score, cha_score]
    scores = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]
    print("You will be assigning scores to your STR, DEX, CON, INT, WIS, CHA from the standard array displayed below:")
    score_array = PrettyTable(["Score", "Modifier"])
    score_array.add_row([15, 2])
    score_array.add_row([14, 2])
    score_array.add_row([13, 1])
    score_array.add_row([12, 1])
    score_array.add_row([10, 0])
    score_array.add_row([8, -1])
    print(score_array)
    iteration = 1
    for x in scores:
        print(standard_array)
        score_choice = input("What score would you like to assign the " + str(x) + " value? ").upper()
        try:
            score_choice = int(score_choice)
        except:
            print("Not an integer")
            while type(score_choice) != int:
                print(standard_array)
                score_choice = input("What score would you like to assign the " + str(x) + " value? ").upper()
                try:
                    score_choice = int(score_choice)
                except:
                    print("Not an integer")
        score_choice = int(score_choice)
        while score_choice not in standard_array:
            print("Select a score that is available.")
            print(standard_array)
            score_choice = input("What score would you like to assign the " + str(x) + " value? ").upper()
            try:
                score_choice = int(score_choice)
            except:
                print("Not an integer")
            score_choice = int(score_choice)
        if iteration == 1:
            str_score = score_choice
        elif iteration == 2:
            dex_score = score_choice
        elif iteration == 3:
            con_score = score_choice
        elif iteration == 4:
            int_score = score_choice
        elif iteration == 5:
            wis_score = score_choice
        elif iteration == 6:
            cha_score = score_choice
        iteration += 1
        standard_array.remove(score_choice)