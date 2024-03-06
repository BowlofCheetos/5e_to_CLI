from global_vars import *

#modifier assign
def mod_assign(score):
    global str_mod, dex_mod, con_mod, int_mod, wis_mod, cha_mod, modifier_output
    if score == 1:
        modifier_output = -5
    elif score > 1 and score < 4:
        modifier_output = -4
    elif score > 3 and score < 6:
        modifier_output = -3
    elif score > 5 and score < 8:
        modifier_output = -2
    elif score > 7 and score < 10:
        modifier_output = -1
    elif score > 9 and score < 12:
        modifier_output = 0
    elif score > 11 and score < 14:
        modifier_output = 1
    elif score > 13 and score < 16:
        modifier_output = 2
    elif score > 15 and score < 18:
        modifier_output = 3
    elif score > 17 and score < 20:
        modifier_output = 4
    elif score > 19 and score < 22:
        modifier_output = 5
    elif score > 21 and score < 24:
        modifier_output = 6
    elif score > 23 and score < 26:
        modifier_output = 7
    elif score > 25 and score < 28:
        modifier_output = 8
    elif score > 27 and score < 30:
        modifier_output = 9
    else:
        modifier_output = 10