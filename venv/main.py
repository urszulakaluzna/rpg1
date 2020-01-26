from person import *
from agresors import *
from gra import *

import random

magic = [{"name": "Fire", "cost": 10, "dmg": 60},
         {"name": "Thunder", "cost": 10, "dmg": 80},
         {"name": "Blizzard", "cost": 10, "dmg": 60}]


running = True
i = 0

while running:
    print("____________________________")

    n = Gracz(input("Podaj swoje imie bohaterze: "), int(input("Wybierz postać: 1-Wojownik lub 2-Mag \n")))
    print(n)
    n.choice()
    player = n.choice()

    print("Wchodzisz do podziemnych katakumb. Wszędzie unosi się ciężki zapach kurzu i pleśni.")
    print("Korytarz rozdziela się na trzy przejścia, wybierz swoją drogę...")

    ch2 = Enemy(int(input("1-korytarz po lewej, 2-środkowy korytarz, 3-korytarz po prawej.\n")))
    print(ch2)
    ch2.ch()
    enemy = ch2.ch()

    while running:
        print("======================")
        choice3 = input("Wybierz działanie:")
        index = int(choice3) - 1

        if index == 0:
            dmg = player.generate_damage()
            enemy.take_damage(dmg)
            print ("Zaatakowałeś za ", dmg, " punktów. Punkt życia wroga: ", enemy.get_hp())

            enemy_choice = 1

            enemy_dmg = enemy.generate_damage()
            player.take_damage(enemy_dmg)
            print("Wróg atakauje za ", enemy_dmg, "Pozostałe punkty życia ", player.get_hp())

            if enemy.get_hp() == 0:
                print(bcolors.OKGREEN + "Wygrałeś!" + bcolors.ENDC)
                running = False
            elif player.get_hp() == 0:
                print(bcolors.FAIL + " Zostałeś pokonany!" + bcolors.ENDC)
                running = False
