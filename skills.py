from global_vars import *

def skill_check(skill, difficulty):
    if skill in str_skills:
        d20()
        from global_vars import roll_result
        if skill in proficient_skills:
            skill_check_result = roll_result + str_mod + prof_bonus
        else:
            skill_check_result = roll_result + str_mod
        print(skill_check_result)
        if skill_check_result >= difficulty:
            print("You have passed the skill check.")
            skill_result = True
        else:
            print("You have failed the check.")
            skill_result = False

skill_check(athletics, 10)