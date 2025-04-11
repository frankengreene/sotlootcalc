import random
import math
import datetime

treasure = {'Treasure Chests': 385, 'Castaway’s Chest': 95, 'Seafarer’s Chest': 200, 'Marauder’s Chest': 400, 'Captain’s Chest': 830, "Coral Castaway's Chest": 166.5,
            "Coral Seafarer's Chest": 350, "Coral Marauder's Chest": 700, "Coral Captain's Chest": 1452.5, "Ashen Castaway's Chest": 200, "Ashen Seafarer's Chest": 400, "Ashen Marauder's Chest": 830,
            "Ashen Captain's Chest": 1600, 'Chest of the Damned': 1080, 'Skeleton Captain’s Chest': 1350, 'Stronghold Chest': 2250, 'Chest of Ancient Tributes': 3650,
            'Chest of Fortune': 20000, 'Chest of a Thousand Grogs': 2400, 'Chest of Sorrow': 3250, 'Chest of Rage': 3250, 'Chest of Everlasting Sorrow': 6500, 'Ancient Goblet': 95,
            'Bronze Secret-Keeper': 95, 'Mysterious Vessel': 95, 'Decorative Coffer': 200, 'Elaborate Flagon': 200, 'Silvered Cup': 200, 'Gilded Chalice': 400, 'Golden Reliquary': 400, 'Ornate Carafe': 400,
            'Adorned Receptacle': 830, 'Opulent Curio': 830, 'Peculiar Relic': 830, 'Mysterious Coral Vessel': 166.5, 'Silvered Coral Cup': 350, 'Golden Coral Reliquary': 700, 'Peculiar Coral Relic': 1452.5,
            'Roaring Goblet': 200, 'Brimstone Casket': 400, 'Devil’s Remnant)t': 830, 'Magma’s Grail': 1600, 'Stone Treasure Vault Keys': 1300, 'Silver Treasure Vault Keys': 2350, 'Gold Treasure Vault Keys': 3675,
            'Sapphire Mermaid Gem': 1000, 'Emerald Mermaid Gem': 1500, 'Ruby Mermaid Gem': 2000, 'Sapphire Siren Gem': 1000, 'Emerald Siren Gem': 1500, 'Ruby Siren Gem': 2000, 'Sapphire Breath of the Sea': 4000,
            'Emerald Breath of the Sea': 6000, 'Ruby Breath of the Sea': 8000, 'Foul Bounty Skull': 135, 'Disgraced Bounty Skull': 265, 'Hateful Bounty Skull': 550, 'Villainous Bounty Skull': 1100, 'Foul Coral Skull': 236.5,
            'Disgraced Coral Skull': 464, 'Hateful Coral Skull': 963, 'Villainous Coral Skull': 1925.5, 'Ashen Foul Bounty Skull': 265, 'Ashen Disgraced Bounty Skull': 550, 'Ashen Hateful Bounty Skull': 1100,
            'Ashen Villainous Bounty Skull': 2125, 'Skeleton Captain’s Skull': 1525, 'Stronghold Skull': 3000, 'Ashen Winds Skull': 10000, 'Skull of the Damned': 1150, 'Captain Skull of the Damned': 2325,
            'Resource Crates': 850, 'Storage Crate of the Damned': 1000, 'Firework Crate': 1550, 'Ammo Crate': 400, 'Firebomb Crate': 1550, 'Highest Quality': 1400, 'Okay Quality': 1000, 'Bad Quality': 600,
            'Worst Quality': 200, 'Crate of Fine Sugar': 150, 'Crate of Rare Tea': 365, 'Crate of Exotic Silks': 750, 'Crate of Exquisite Spices': 1500, 'Crate of Ancient Bone Dust': 3750, 'Crate of Volcanic Stone': 365,
            'Crate of Fine Ore': 750, 'Crate of Extraordinary Minerals': 1500, 'Crate of Precious Gemstones': 2850, 'Ashes of the Damned': 1275, 'Cannonball Crate of the Damned': 1000, 'Gunpowder Barrel': 150,
            'Stronghold Gunpowder Barrel': 4375, 'Keg of Ancient Black Powder': 4000, 'Coffer of Aged Grog': 150, 'Coffer of Antiquated Coffee': 365, 'Coffer of Timeworn Metals': 750, 'Coffer of Forgotten Jewels': 1500,
            'Chest of Legends': 9800, 'Ashen Chest of Legends': 14000, 'Chalice of Ancient Fortune': 595, 'Gilded Relic of Ancient Fortune': 1475, 'Skull of Ancient Fortune': 595, 'Villainous Skull of Ancient Fortune': 1475,
            'Crate of Legendary Voyages': 595, "Jar of Athena's Incense": 1475, 'Offering of Legendary Goods': 2625, 'Legendary Fortune Keeper': 2625, 'Artifact of Legendary Hunger': 2625, "Athena's Relic": 3650, "Skull of Athena's Blessing": 3700,
            'Skull of Destiny': 10, 'Humble Gift': 5, 'Generous Gift': 10, 'Reaper’s Chest': 25, 'Reaper’s Bounty': 10000, 'Box of Wondrous Secrets': 25000, 'Broken Emissary Flag Grade I': 2000, 'Broken Emissary Flag Grade II': 4000,
            'Broken Emissary Flag Grade III': 6000, 'Broken Emissary Flag Grade IV': 8000, 'Broken Emissary Flag Grade V': 10000, 'Ashen Key': 5, 'Ashen Chest': 5, 'Ashen Tomes': 10, 'Ritual Skull': 10, 'Rag & Bone Crates': 5,
            'Trident of the Dark Tides': 250, 'Talisman of Great Fortunes': 10000, 'Corrupted Bounty Skull': 2450, 'Bewitching Doll': 1700, 'Mutinous Effigy': 1700, "Sea Master's Chest": 1500}

emissary_bonus = {"1": 0, "2": .33, "3": .67, "4": 1.00, "5": 1.50 }

quests = ["Fof", "Capmap", "Skelly bounty", "Athena fort"]

companies = ["Reaper's Bones", "Athena's Fortune", "Hunter's Call", "Order of Souls", "Merchant Alliance", "Gold Hoarders", "Guild"]

reward = 0

is_running = True

now = datetime.datetime.now()
current_hour = now.hour

gold_rush = False
if 21 <= current_hour <= 22 or 13 <= current_hour <= 16:
    gold_rush = True


   # elif status == "Bounty":
  #      reward = treasure["Skull"] + treasure["Gem"]
 #       print(f"You earned {reward} gold!")
#    else:
 #       reward = treasure["Gem"] * 2 + treasure["Skull"]
#        print(f"You earned {reward} gold!")

# 🦜 🏴‍☠️


while is_running:
    print("""
  /$$$$$$            /$$   /$$
 /$$__  $$          | $$  | $$
| $$  \__/  /$$$$$$ | $$ /$$$$$$   /$$   /$$
|  $$$$$$  |____  $$| $$|_  $$_/  | $$  | $$
 \____  $$  /$$$$$$$| $$  | $$    | $$  | $$
 /$$  \ $$ /$$__  $$| $$  | $$ /$$| $$  | $$
|  $$$$$$/|  $$$$$$$| $$  |  $$$$/|  $$$$$$$
 \______/  \_______/|__/   \___/   \____  $$
                                   /$$  | $$
                                  |  $$$$$$/
                                   \______/
 /$$$$$$$$
| $$_____/
| $$    /$$   /$$ /$$$$$$$   /$$$$$$   /$$$$$$$
| $$$$$| $$  | $$| $$__  $$ /$$__  $$ /$$_____/
| $$__/| $$  | $$| $$  \ $$| $$  \ $$|  $$$$$$
| $$   | $$  | $$| $$  | $$| $$  | $$ \____  $$
| $$   |  $$$$$$/| $$  | $$|  $$$$$$$ /$$$$$$$/
|__/    \______/ |__/  |__/ \____  $$|_______/
                            /$$  \ $$
                           |  $$$$$$/
                            \______/
  /$$$$$$            /$$
 /$$__  $$          | $$
| $$  \ $$ /$$$$$$$ | $$ /$$   /$$
| $$  | $$| $$__  $$| $$| $$  | $$
| $$  | $$| $$  \ $$| $$| $$  | $$
| $$  | $$| $$  | $$| $$| $$  | $$
|  $$$$$$/| $$  | $$| $$|  $$$$$$$
 \______/ |__/  |__/|__/ \____  $$
                         /$$  | $$
                        |  $$$$$$/
                         \______/
""")
    print("🏴‍☠️🏴‍☠️🏴‍☠️🏴‍☠️🏴‍☠️🏴‍☠️ SALTY FUNG'S WEALTH ABACUS  🏴‍☠️🏴‍☠️🏴‍☠️🏴‍☠️🏴‍☠️🏴‍☠️\n")
    print("Welcome to the Salty Fungs Wealth Abacus. For all intents and purposes")
    print('it is assumed you are sailing as a Guild Emissary, and a list of available')
    print('voyages can be accessed using !help at any time.\nIt is also assumed you are completing the highest rank voyage.\n')
    if gold_rush:
        print("💰🔱💰🔱💰🔱 IT'S GOLD RUSH TIME 🔱💰🔱💰🔱💰")
    status = input("What quest would you like to do? (X to quit): ").capitalize()

    if status == "!help":
        print(quests)

    if status == "X":
        print("SALTY FUNGS ONLY!")
        is_running = False
        break
    if status not in quests:
        while status not in quests:
            print("Try again, fumb duck.")
            status = input("What quest would you like to do? (X to quit): ").capitalize()
            if status == "X":
                print("SALTY FUNGS ONLY!")
                is_running = False
                break

    company = 'Guild'
   # company = input("What company are you sailing for?: ").capitalize()
    #if company not in companies:
      #  print("Try again, fumb duck.")

    if status == "Athena fort":
        init_reward = ((treasure["Crate of Legendary Voyages"] * 3) + treasure["Legendary Fortune Keeper"] + (2 * treasure["Skull of Athena's Blessing"]) + treasure["Treasure Chests"] + treasure["Skull of Ancient Fortune"] + treasure["Artifact of Legendary Hunger"] + treasure["Talisman of Great Fortunes"]) + treasure["Stronghold Skull"] + (treasure["Villainous Bounty Skull"] * 2) + treasure["Chalice of Ancient Fortune"]
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
             reward + gr_bonus
        print(f"🦜 Your estimated earning from completing a {status} at Grade {emi} {company} is {reward:.0f} gold!💰")
        is_running = False













