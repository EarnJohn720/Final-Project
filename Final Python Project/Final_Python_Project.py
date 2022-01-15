import os, datetime, random, Classes
print(os.environ['USERPROFILE'])
user = (os.getenv('username'))
current_time = datetime.datetime.now()
format_time = current_time.strftime("%d/%m/%Y %H:%M:%S")
print(format_time)


def main():
    choice = ""
    alignments = ["Lawful Good", "Neutral Good", "Chaotic Good",
                  "Lawful Neutral", "True Neutral", "Chaotic Neutral",
                  "Lawful Evil", "Neutral Evil", "Chaotic Evil"]
    races = ["Dragonborn", "Gnome", "Dwarf", "Half-Elf", "Elf", "Halfling", "Half-Orc", "Human", "Tiefling"]
    stats = {"Strength" : 0, "Dexterity" : 0, "Constitution" : 0, "Intelligence" : 0, "Wisdom" : 0, "Charisma" : 0}
    try:
        CharAmt = int(input("How many characters do you want to make?: "))
    except :
        print("Please enter a valid nuber.")
    
    name = input("Enter your character name: ")
    age = int(input("Enter your character age: "))
    race = ""
    #for x in range(len(races)):
    #    print(f"{x + 1}. {races[x]}")
    print("There are 9 races:\n1. Dragonborn, 2. Gnome, 3. Dwarf,\n")
    print("4. Half-Elf, 5. Elf, 6. Halfling,\n")
    print("7. Half-Orc, 8. Human, 9. Tiefling")
    race = int(input("Choose your character race: "))
    match race:
            case 1:
                race = races[race - 1]
            case 2:
                race = races[race - 1]
            case 3:
                race = races[race - 1]
            case 4:
                race = races[race - 1]
            case 5:
                race = races[race - 1]
            case 6:
                race = races[race - 1]
            case 7:
                race = races[race - 1]
            case 8:
                race = races[race - 1]
            case 9:
                race = races[race - 1]
    print("There are 6 alignments:\n1. Lawful Good, 2. Neutral Good, 3. Chaotic Good,\n")
    print("4. Lawful Neutral, 5. True Neutral, 6. Chaotic Neutral,\n")
    print("7. Lawful Evil, 8. Neutral Evil, 9. Chaotic Evil")
    align = input("Choose your character alignment (Enter any number between  1 - 6): ")
    match align:
            case 1:
                choice = alignments[align - 1]
            case 2:
                choice = alignments[align - 1]
            case 3:
                choice = alignments[align - 1]
            case 4:
                choice = alignments[align - 1]
            case 5:
                choice = alignments[align - 1]
            case 6:
                choice = alignments[align - 1]
            case 7:
                choice = alignments[align - 1]
            case 8:
                choice = alignments[align - 1]
            case 9:
                choice = alignments[align - 1]

            
    party = []
    while True:
        for x in stats.keys():
            stats[x] = random.randint(1, 10)
        for x, y in stats.items():
            print(f"{x}: {y}")
        stat_change = input("Are you okay with these stats?(Enter Y for yes/Any other key to randomize): ")
        if stat_change.upper() == "Y":
            break
        else:
            continue

    for x in range(CharAmt):
        party.append(Classes.Character(name, age, race, choice, stats))
    #test = len(stats)
    #for x in stats.keys():
    #    stats[x] = random.randint(1, 10)

    

    


main()
