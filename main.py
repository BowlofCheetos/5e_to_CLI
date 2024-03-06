from global_vars import *
from player_intro import *
from race_info import *
from score_assign import *
from modifier_assign import *

#introduction
intro()
player_name()

#score selection
score_assign()
print(str_score)
print(dex_score)
print(con_score)
print(int_score)
print(wis_score)
print(cha_score)

#modifier generation
mod_assign(str_score)
str_mod = modifier_output
print(str_mod)
mod_assign(dex_score)
dex_mod = modifier_output
mod_assign(con_score)
con_mod = modifier_output
mod_assign(int_score)
int_mod = modifier_output
mod_assign(wis_score)
wis_mod = modifier_output
mod_assign(cha_score)
cha_mod = modifier_output

#race info
race_info()

#race traits
