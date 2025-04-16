def calculate_reward(init_reward_func, status, treasure, emissary_bonus, company, gold_rush):
    init_reward = init_reward_func(treasure)
    emi = input("What is your emissary grade?: ").capitalize()
    if emi not in emissary_bonus and emi != "X":
        print("Try again, fumb duck.")
        emi = input("What is your emissary grade?: ").capitalize()
    if emi == "X":
        print("SALTY FUNGS ONLY!")
        return None

    reward = init_reward
    if company == 'Guild':
        grade_bonus = {"2": 0.33, "3": 0.67, "4": 1.00, "5": 1.50}
        if emi in grade_bonus:
            reward += init_reward * grade_bonus[emi]

    if gold_rush:
        reward += init_reward * 1.50

    return reward, emi