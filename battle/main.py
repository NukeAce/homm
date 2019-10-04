from classes.game  import person, colors
from classes.magic import spell
from classes.items import Item
import random as rd


#create black magic
Fire = spell("fire", 10, 100, "black")
Thunder = spell("thunder", 10, 100, "black")
blizzard = spell("Blizzard", 10, 100, "black")
Meteor = spell("meteor", 10, 100, "black")
Quake = spell("Quake", 120, 140, "black")


#create white magic
cure = spell("cure", 12, 120, "white")
cura = spell("cura",18, 200, "white")

#create item
potion = Item("potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-potion", "potion", "Heals 50 HP", 50)
superpotion = Item("Super-potion", "potion", "Heals 50 HP", 50)
elixr = Item("elixr", "elixr", "fully restores HP/HP of one party member", 9999)
superelixr = Item("MegaElixr", "elixr", "fully restores HP/HP of entire party member", 9999)

grenade = Item("grenade", "attack", "Deals 500 damage", 500)



player_spells =[Fire,Thunder,blizzard,Meteor,Quake,cure,cura]
enemy_spells = [Fire, Thunder, cura]
player_items = [{"item":potion, "quantity": 12},{"item": hipotion, "quantity": 4},
                {"item":superpotion, "quantity":2}, {"item":elixr, "quantity": 5}, 
                {"item":superelixr, "quantity": 3},{"item":grenade, "quantity":1}]



#instantiate people
Player1 = person("Valos", 13400, 265, 160, 4260, player_spells, player_items)
Player2 = person("Nick ", 134, 265, 160, 4260, player_spells, player_items)
Player3 = person("Robot", 134, 265, 160, 4260, player_spells, player_items)

enemy2 = person("Imp  ",560,325,25,1250,[], [])
enemy1 = person("Magus",701,525,65,11200,[], [])
enemy3 = person("Imp  ",560,325,65,1250,[], [])



Players =[Player1,Player2,Player3]
enemies = [enemy1,enemy2,enemy3]



running = True
i=0
print("\n \n")
print (colors.BOLD + colors.FAIL+"AN ENEMY ATTACKS"+colors.ENDC)

while running:
    print("===============================================================")
    print("\n")
    print("NAME          HP                                   MP")  
    for Player in Players:  
        Player.get_stats()
    
    for enemy in enemies:
        enemy.get_enemy_stats()


    

    print("\n") 

    for Player in Players:
        Player.choose_action()
        choice = input("    Choose action: ")
        
        
        index = int(choice) - 1

        if index ==0:
            dmg = Player.generate_damage()
            enemy=Player.choose_target(enemies)

            enemies[enemy].take_damage(dmg)
            print(Player.name + " attacked "+enemies[enemy].name.replace(" ","")+ " for", dmg, "points of damage.")

            if enemies[enemy].get_hp()==0:
                print(enemies[enemy].name.replace(" ","") + " has died.")
                del enemies[enemy]
        elif index == 1:
            Player.choose_magic()

            magic_choice = int(input("    Choose magic: "))-1

            if magic_choice ==-1:
                continue

            spell = Player.magic[magic_choice]
            magic_dmg = Player.magic[magic_choice].generate_spelldamage()


            current_mp = Player.get_mp()

            if spell.cost > current_mp:
                print(colors.FAIL +"\nYour mp isnt enough\n"+ colors.ENDC)
                continue
            Player.reduce_mp(spell.cost)

            if spell.type == "white":
                Player.heal(magic_dmg)
                print(colors.OKBLUE + "\n " + spell.name + " heals for", str(magic_dmg), "points." + colors.ENDC)
            
            elif spell.type == "black":
                enemy=Player.choose_target(enemies)
                enemies[enemy].take_damage(magic_dmg)
                print(Player.name + " attacked"+ "for", magic_dmg, "points of damage.")
                if enemies[enemy].get_hp()==0:
                    print(enemies[enemy].name.replace(" ","") + " has died.")
                    del enemies[enemy]

        elif index ==2:
            Player.choose_items()

            item_choice = int(input("    Select item: "))-1

            if item_choice == -1:
                continue

            item = Player.item[item_choice]["item"]
            if Player.item[item_choice]["quantity"] ==0:
                print(colors.FAIL + "You've run out of", item.name + "s"+ colors.ENDC)
                continue


        
            Player.item[item_choice]["quantity"]-=1
        
        
            if item.type == "potion":
                Player.heal(item.prop)
                print(colors.OKGREEN +"\n"+ item.name+ " heals for", str(item.prop), "HP" + colors.ENDC)
            
            elif item.type =="elixr":
                    if item.name == "MegaElixr":
                        for i in Players:
                            i.hp = i.maxhp
                            i.mp = i.maxmp
                    
                    else:
                        Player.hp = Player.maxhp
                        Player.mp =Player.maxmp
                    print(colors.OKGREEN +"\n"+ item.name + " fully restores HP/HP" + colors.ENDC)

            elif item.type == "attack":
                enemy=Player.choose_target(enemies)
                enemies[enemy].take_damage(item.prop)
                print(colors.FAIL + "\n " + item.name + " deals for", str(item.prop), "points on"+ enemies[enemy].name + colors.ENDC)
                if enemies[enemy].get_hp()==0:
                    print(enemies[enemy].name.replace(" ","") + " has died.")
                    del enemies[enemy]               
        

        elif index >= 3:
            print("    Invalid input try again")
            continue    



    defeated_enemies =0
    defeated_players =0

    for enemy in enemies:
        if enemy.get_hp ==0:
            defeated_enemies += 1


    if defeated_enemies ==1:
        print(colors.OKGREEN+"you win"+colors.ENDC)
        running = False

    elif defeated_players ==3:
        print(colors.FAIL+"you lose"+colors.ENDC)
        running = False



    #enemy attack phase
    for enemy in enemies:

        enemy_choice = rd.randrange(0,3)
        
        if enemy_choice ==0:

            target = rd.randrange(0,3)
            enemy_dmg = enemies[0].generate_damage()
            Players[target].take_damage(enemy_dmg)
            print(enemy.name.replace(" ","") + " attacks"+ Players[target].name+" for"+str(enemy_dmg) + " points")

        elif enemy_choice ==1:

            spell, magic_dmg = enemy.choose_enemy_spell()
            enemy.reduce_mp(spell.cost)
            print("Enemy chose", spell, "damage is", magic_dmg)

            if spell.type == "white":
                enemy.heal(magic_dmg)
                print(colors.OKBLUE + "\n " + spell.name + " heals"+enemy.name + "for", str(magic_dmg), "points." + colors.ENDC)
            
            elif spell.type == "black":
                target = rd.randrange(0,3)
                Players[target].take_damage(magic_dmg)
                print(enemy.name.replace(" ","") + " attacked for", magic_dmg, "points of damage.")
                if Players[target].get_hp()==0:
                    print(Players[target].name.replace(" ","") + " has died.")
                    del Players[target]
            print ("Enemy chose", spell,"damage is", magic_dmg)


