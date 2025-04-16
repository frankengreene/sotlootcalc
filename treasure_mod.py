if status == "Athena fort":
    init_reward = ((treasure["Crate of Legendary Voyages"] * 3) + treasure["Legendary Fortune Keeper"] + (
                2 * treasure["Skull of Athena's Blessing"]) + treasure["Treasure Chests"] + treasure[
                       "Skull of Ancient Fortune"] + treasure["Artifact of Legendary Hunger"] + treasure[
                       "Talisman of Great Fortunes"]) + treasure["Stronghold Skull"] + (
                              treasure["Villainous Bounty Skull"] * 2) + treasure["Chalice of Ancient Fortune"]
    emi = input("What is your emissary grade?: ").capitalize()
    if emi not in emissary_bonus and emi != "X":
        print("Try again, fumb duck.")
        emi = input("What is your emissary grade?: ").capitalize()
    elif emi == "X":
        print("SALTY FUNGS ONLY!")
        is_running = False
        break
    if company == "Guild":
        if emi == '1':
            reward = init_reward
        if emi == '2':
            bonus = init_reward * .33
            reward = init_reward + bonus
        elif emi == '3':
            bonus = init_reward * .67
            reward = init_reward + bonus
        elif emi == '4':
            bonus = init_reward * 1.00
            reward = init_reward + bonus
        elif emi == '5':
            bonus = init_reward * 1.50
            reward = init_reward + bonus
    if gold_rush:
        gr_bonus = init_reward * 1.50
        reward + gr_bonus
    print(f"🦜 Your estimated earning from completing a {status} at Grade {emi} {company} is {reward:.0f} gold!💰")
    is_running = False

if status == "Capmap":
    init_reward = ((treasure["Sea Master's Chest"]) * 3)
    emi = input("What is your emissary grade?: ").capitalize()
    if emi not in emissary_bonus and emi != "X":
        print("Try again, fumb duck.")
        emi = input("What is your emissary grade?: ").capitalize()
    elif emi == "X":
        print("SALTY FUNGS ONLY!")
        is_running = False
        break
    if company == "Guild":
        if emi == '2':
            bonus = init_reward * .33
            reward = init_reward + bonus
        elif emi == '3':
            bonus = init_reward * .67
            reward = init_reward + bonus
        elif emi == '4':
            bonus = init_reward * 1.00
            reward = init_reward + bonus
        elif emi == '5':
            bonus = init_reward * 1.50
            reward = init_reward + bonus
    if gold_rush:
        gr_bonus = init_reward * 1.50
        reward + gr_bonus
    print(f"🦜 Your estimated earning from completing a {status} at Grade {emi} {company} is {reward:.0f} gold!💰")
    is_running = False

if status == "Skelly bounty":
    init_reward = (treasure["Corrupted Bounty Skull"] + (treasure['Mutinous Effigy']) * 3)
    emi = input("What is your emissary grade?: ").capitalize()
    if emi not in emissary_bonus and emi != "X":
        print("Try again, fumb duck.")
        emi = input("What is your emissary grade?: ").capitalize()
    elif emi == "X":
        print("SALTY FUNGS ONLY!")
        is_running = False
        break
    if company == "Guild":
        if emi == '2':
            bonus = init_reward * .33
            reward = init_reward + bonus
        elif emi == '3':
            bonus = init_reward * .67
            reward = init_reward + bonus
        elif emi == '4':
            bonus = init_reward * 1.00
            reward = init_reward + bonus
        elif emi == '5':
            bonus = init_reward * 1.50
            reward = init_reward + bonus
    if gold_rush:
        gr_bonus = init_reward * 1.50
        reward + gr_bonus
    print(f"🦜 Your estimated earning from completing a {status} at Grade {emi} {company} is {reward:.0f} gold!💰")
    is_running = False

if status == "Fof":
    init_reward = (treasure["Chest of Fortune"] + treasure["Chest of Legends"] + (
            2 * treasure["Keg of Ancient Black Powder"]) + (4 * treasure["Crate of Legendary Voyages"]) + (
                           random.randrange(4, 8) * treasure["Gilded Relic of Ancient Fortune"]) + (
                       random.randrange(0, 4)) * treasure["Chalice of Ancient Fortune"]) + (
                          random.randrange(1, 3) * treasure["Villainous Skull of Ancient Fortune"]) + (
                          random.randrange(0, 1) * treasure["Skull of Ancient Fortune"]) + (
                          3 * treasure["Stronghold Chest"]) + (2 * treasure["Crate of Ancient Bone Dust"]) + \
                  treasure["Stronghold Skull"] + (3 * treasure["Captain’s Chest"]) + sum(
        treasure[random.choice(["Crate of Rare Tea", "Crate of Fine Sugar", "Crate of Exotic Silks"])] for _ in
        range(3)) + sum(
        treasure[random.choice(["Sapphire Mermaid Gem", 'Emerald Mermaid Gem', 'Ruby Mermaid Gem'])] for _ in
        range(5))
    emi = input("What is your emissary grade?: ").capitalize()
    if emi not in emissary_bonus and emi != "X":
        print("Try again, fumb duck.")
        emi = input("What is your emissary grade?: ").capitalize()
    elif emi == "X":
        print("SALTY FUNGS ONLY!")
        is_running = False
        break
    if company == "Guild":
        if emi == '2':
            bonus = init_reward * .33
            reward = init_reward + bonus
        elif emi == '3':
            bonus = init_reward * .67
            reward = init_reward + bonus
        elif emi == '4':
            bonus = init_reward * 1.00
            reward = init_reward + bonus
        elif emi == '5':
            bonus = init_reward * 1.50
            reward = init_reward + bonus
    if gold_rush:
        gr_bonus = init_reward * 1.50
        reward = reward + gr_bonus
    print(f"🦜 Your estimated earning from completing a {status} at Grade {emi} {company} is {reward:.0f} gold!💰")
    is_running = False