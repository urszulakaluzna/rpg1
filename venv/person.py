import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Mag:

    def __init__(self, hp, mp, atk ,df, magic):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 20
        self.atkh = atk + 20
        self.df = df
        self.magic = magic
        self.action = ["Atak", "Magia"]

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def generate_spell_damage(self, i):
        mgh = self.magic[i]["dmg"]-5
        mgl = self.magic[i]["dmg"]+5
        return random.randrange(mgh, mgl)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp


    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self):
        self.mp -= cost

    def get_spell_name(self, i):
        return self.magic[i]["name"]

    def get_spell_mp_cost(self, i):
        return self.magic[i]["cost"]


class Gracz:
    def __init__(self, name, choice1):

        self.name = name
        self.choice1 = choice1

    def choice(self):

        if self.choice1 == 1:
            player = Mag(100, 100, 100, 110, 100)
            print("Twój bohater to Wojownik.")
            return player

        elif self.choice1 == 2:
            player = Mag(10, 110, 10, 100, 120)
            print("Twój bohater to Mag.")
            return player

        else:
            print("Wybierz klasę")
