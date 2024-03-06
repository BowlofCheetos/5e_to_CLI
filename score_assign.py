from global_vars import *
from prettytable import PrettyTable

#score selection
def score_selection():
    global str_score, dex_score, con_score, int_score, wis_score, cha_score, score_choice
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
        standard_array.remove(score_choice)
        plr_scores[0] = score_choice
        plr_scores.pop(0)

score_selection()

print(str(str_score))
print(str(dex_score))
print(str(con_score))
print(str(int_score))
print(str(wis_score))
print(str(cha_score))