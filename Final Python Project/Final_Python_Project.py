import os, datetime, random, Classes
print(os.environ['USERPROFILE'])
user = (os.getenv('username'))
current_time = datetime.datetime.now()
format_time = current_time.strftime("%d/%m/%Y %H:%M:%S")
print(format_time)


def main():
    your_race_des = ""
    race_descripts = ["Dragonborn look very much like dragons standing errect in humaniod form, though they lack wings or a tail",
                     "A gnome's energy and ethusiasm for living shines through every inch of his or her tiny body.",
                     "Bold and hardy, dwarves are known as skilled warriors, miners, and workers of stone and metal.",
                     "Half-elves cobine what some say are the best qualities of their elf and human parents.",
                     "Elves are a magical people of otherworldly grace, living in the world but not entirely part of it.",
                     "The diminutive halflings survive in a world full of larger creatures by avoiding notice or barring that, avoiding offense.",
                     "Halforcs' grayish pigmentation sloping forehead, jutting jaws, prominent teeth, and towering builds make their orcish heritage plan for all to see.",
                     "Humans are the most adaptable and ambitious people among the common races. Whatever drives them, humans are the innovators, the achievers, and the pioneers of worlds.",
                     "To be greeted with stares and whispers, to suffer violence and insult on the street, to see mistrust and fear in every eye: this is the lot of the tiefling."]
    choice = ""
    party = []

    alignments = ["Lawful Good", "Neutral Good", "Chaotic Good",
                  "Lawful Neutral", "True Neutral", "Chaotic Neutral",
                  "Lawful Evil", "Neutral Evil", "Chaotic Evil"]
    races = ["Dragonborn", "Gnome", "Dwarf", "Half-Elf", "Elf", "Halfling", "Half-Orc", "Human", "Tiefling"]
    stats = {"Strength" : 0, "Dexterity" : 0, "Constitution" : 0, "Intelligence" : 0, "Wisdom" : 0, "Charisma" : 0}
    while True:
        try:
            CharAmt = int(input("How many characters do you want to make?: "))
            break
        except :
            print("Please enter a valid nuber. Restarting")
            continue
    
    for x in range(CharAmt):
        name = input("Enter your character name: ")
        while True:
            try:
                age = int(input("Enter your character age: "))
                race = 0
                
                print("There are 9 races:\n1. Dragonborn, 2. Gnome, 3. Dwarf,")
                print("4. Half-Elf, 5. Elf, 6. Halfling,")
                print("7. Half-Orc, 8. Human, 9. Tiefling")
                race = int(input("Choose your character race: "))
                your_race_des = race_descripts[race - 1]
                match race:
                        case 1:
                            race = races[race - 1]
                            #your_race_des = race_descripts[race - 1]
                            #print(your_race_des)
                        case 2:
                            race = races[race - 1]
                            #your_race_des = race_descripts[race - 1]
                            #print(your_race_des)
                        case 3:
                            race = races[race - 1]
                            #your_race_des = race_descripts[race - 1]
                            #print(your_race_des)
                        case 4:
                            race = races[race - 1]
                            #your_race_des = race_descripts[race - 1]
                            #print(your_race_des)
                        case 5:
                            race = races[race - 1]
                            #your_race_des = race_descripts[race - 1]
                            #print(your_race_des)
                        case 6:
                            race = races[race - 1]
                            #your_race_des = race_descripts[race - 1]
                            #print(your_race_des)
                        case 7:
                            race = races[race - 1]
                            #your_race_des = race_descripts[race - 1]
                            #print(your_race_des)
                        case 8:
                            race = races[race - 1]
                            #your_race_des = race_descripts[race - 1]
                            #print(your_race_des)
                        case 9:
                            race = races[race - 1]
                            #your_race_des = race_descripts[race - 1]
                            #print(your_race_des)
                print(your_race_des)
                print("There are 6 alignments:\n1. Lawful Good, 2. Neutral Good, 3. Chaotic Good,")
                print("4. Lawful Neutral, 5. True Neutral, 6. Chaotic Neutral,")
                print("7. Lawful Evil, 8. Neutral Evil, 9. Chaotic Evil")
                align = int(input("Choose your character alignment (Enter any number between  1 - 6): "))
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
                break
            except :
                print("Please enter a valid nuber. Restarting....")
                continue
                
        while True:
            for x in stats.keys():
                stats[x] = random.randint(1, 10)
            for x, y in stats.items():
                print(f"{x}: {y}")
            stat_change = input("Are you okay with these stats?(Enter Y for yes/Any other key to randomize): ")
            if stat_change.upper() == "Y":
                party.append(Classes.Character(name, age, race, your_race_des, choice, stats))
                #party.append(Classes.Character(name, age, race, choice, stats))
                print()
                break
            else:
                continue

    file_open = open("DnD Campaign Characters.txt", "w")
    for x in range(len(party)):
        temp_dict = ""
        file_open.write(f"Name: {party[x].getName()}\n")
        file_open.write(f"Age: {party[x].getAge()}\n")
        file_open.write(f"Race: {party[x].getRace()}\n")
        file_open.write(f"Race Description: {party[x].getDescript()}\n")
        file_open.write(f"Alignment: {party[x].getAlign()}\n")
        temp_dict = party[x].returnStats()
        for z, y in temp_dict.items():
            file_open.write(f"{z}: {y}\n")
        file_open.write("\n")
        print(f"Name: {party[x].getName()}")
        print(f"Age: {party[x].getAge()}")
        print(f"Race: {party[x].getRace()}")
        print(f"Race Description: {party[x].getDescript()}")
        print(f"Alignment: {party[x].getAlign()}")
        party[x].getStats()
        print()

    file_open.close()
main()
