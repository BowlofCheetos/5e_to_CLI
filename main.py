from global_vars import *
from player_intro import *
from race_info import *
from race_traits import *
from score_assign import *
from modifier_assign import *
from skill_check import *

#introduction
intro()
player_name()
from player_intro import *

#score selection
score_assign()
from score_assign import *

#modifier generation
mod_assign(str_score)
from modifier_assign import modifier_output
str_mod = modifier_output
mod_assign(dex_score)
from modifier_assign import modifier_output
dex_mod = modifier_output
mod_assign(con_score)
from modifier_assign import modifier_output
con_mod = modifier_output
mod_assign(int_score)
from modifier_assign import modifier_output
int_mod = modifier_output
mod_assign(wis_score)
from modifier_assign import modifier_output
wis_mod = modifier_output
mod_assign(cha_score)
from modifier_assign import modifier_output
cha_mod = modifier_output

#race info
race_info()
from race_info import *

#race traits
race_selection()
from race_traits import *

skill_check(athletics, 10)
from skill_check import *