from global_vars import *

#modifier assign
def mod_assign(score):
    global str_mod, dex_mod, con_mod, int_mod, wis_mod, cha_mod, modifier_output
    modifier_output = 0
    if score == 1:
        score = -5
    elif score > 1 and score < 4:
        score = -4
    elif score > 3 and score < 6:
        score = -3
    elif score > 5 and score < 8:
        score = -2
    elif score > 7 and score < 10:
        score = -1
    elif score > 9 and score < 12:
        score = 0
    elif score > 11 and score < 14:
        score = 1
    elif score > 13 and score < 16:
        score = 2
    elif score > 15 and score < 18:
        score = 3
    elif score > 17 and score < 20:
        score = 4
    elif score > 19 and score < 22:
        score = 5
    elif score > 21 and score < 24:
        score = 6
    elif score > 23 and score < 26:
        score = 7
    elif score > 25 and score < 28:
        score = 8
    elif score > 27 and score < 30:
        score = 9
    else:
        score = 10
    modifier_output = score
    print(modifier_output)