from person import *
from gra import *

import random

class Enemy:
    def __init__(self, choice2):
        self.choice2 = choice2

    def ch(self):

        if self.choice2 == 1:
            enemy = Vampire(800, 120, 80)
            print("Wybierasz lewy korytarz, poruszając się coraz głębiej napotykasz Wampira.")
            return enemy

        elif self.choice2 == 2:
            enemy = Werewolf(500, 120, 100)
            print("Wybierasz środkowy korytarz, poruszając się coraz głębiej napotykasz Wilkołaka.")
            return enemy

        elif self.choice2 == 3:
            enemy = Undead(500, 120, 120)
            print("Wybiersza korytarz po prawej, idąc w głąb napotykasz Nieuarłego.")

            return enemy

        else:
            print("Wybierz poprawnie korytarz")
            print(bcolors.FAIL + bcolors.BOLD + "\nWróg atakuje!" + bcolors.ENDC)


#class Dragon(self, atk, health):
 #   self.atk = drgon_magic
  #  self.health == 2000


#class Fire(self, atk):
#    self.atk == 100


#class Ghost(self, atk, health):
#    self.atk = random.randrange(30, 40)
#    self.health == 400
    #dopisac odpornosc na atak


#class Skeleton(self, atk, health):
#    self.atk = random.randrange(30, 40)
#    self.health == 400
    #dopisac trafialnosc


class Hound:
    def __init__(self, hp, atk, df):
        self.maxhp = hp
        self.hp = hp
        self.atkl = atk - 20
        self.atkh = atk + 20
        self.df = df


#class Lamia(self, atk, health):
#    self.atk = random.randrange(30, 40)#trucizna
#    self.health == 400


#class Ghoul(self, atk, health):
#    self.atk = random.randrange(30, 40)
#    self.health == 600


#class Pack(self, atk, health):
#    self.atk = random.randrange(20, 30)
#    self.health == 200


#class Imp(self, atk, health):
#    self.atk = random.randrange(20, 30)
#    self.health == 200


class Vampire:
    def __init__(self, hp, atk, df):
        self.maxhp = hp
        self.hp = hp
        self.atkl = atk - 40
        self.atkh = atk + 40
        self.df = df

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def get_hp(self):
        return self.hp


class Undead:
    def __init__(self, hp, atk, df):
        self.maxhp = hp
        self.hp = hp
        self.atkl = atk - 40
        self.atkh = atk + 40
        self.df = df

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def get_hp(self):
        return self.hp

class Werewolf:
    def __init__(self, hp, atk, df):
        self.maxhp = hp
        self.hp = hp
        self.atkl = atk - 40
        self.atkh = atk + 40
        self.df = df

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def get_hp(self):
        return self.hp