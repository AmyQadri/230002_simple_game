import time
import random
class Hero:
    __jumlah = 0

    def __init__(self, inputName, inputHealth, inputAttack):
        self.__name = inputName
        self.level = 0
        self.health = inputHealth
        self.attack = inputAttack
        Hero.__jumlah += 1  
    
    def __str__(self):
        return f"Nama hero : {self.__name}\nLevel Hero : {self.level}\nHealth Hero : {self.health}\nAttack Hero : {self.attack}"    



    @property
    def levelUp(self):
        self.level += 1
        self.attack += self.level * 0.5
    
    @property
    def healing(self):
        i=0
        while (i != 5):
            self.health += 20
            time.sleep(1)
            i += 1
            print(f"Darah {self.__name} : {self.health}")
    
    @property
    def changeName(self):
        pass

    @changeName.setter
    def changeName(self, value):
        print("Nama sebelum di ganti {}".format(self.__name))
        self.__name = value
        print("Nama setelah di ganti {}".format(self.__name))

    @staticmethod
    def war(player1,player2):
        while (player1.health or player2.health >= 0):
            list = [player1,player2]
            pilih = random.choice(list)
            attacker = ""
            deffender = ""
            if (pilih == player1):
                attacker = player1
                deffender = player2
            else:
                deffender = player1
                attacker = player2
            deffender.health -= attacker.attack
            if (deffender.health <= 0):
                print(f"{deffender.__name} telah di eliminasi")
                break
            print(f"{attacker.__name} Menyerang {deffender.__name}")
            print(f"Darah {deffender.__name} sisa : {deffender.health}")
            time.sleep(1)


class Marksman(Hero):
    def __init__(self, inputName, inputHealth, inputAttack):
        super().__init__(inputName, inputHealth, inputAttack)
        self.__role = "Marksman"



miya = Marksman("miya",400,12)
moskov = Hero("moskov",380,14)

Hero.war(miya,moskov)