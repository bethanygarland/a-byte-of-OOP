class Vampire:
    coven = []


    def __init__(self, name, age,in_coffin, drank_blood_today):
        self.name = name
        self.age = age
        self.in_coffin = in_coffin
        self.drank_blood_today = drank_blood_today
        __class__.coven = __class__.coven

    @classmethod
    def create(cls, name, age, in_coffin, drank_blood_today):
        vamp = cls(name, age, in_coffin, drank_blood_today)
        cls.coven.append(vamp)
        return vamp

    def drink_blood(self):
        if self.drank_blood_today == True:
            return f'Coven member "{self.name}" drank blood today.'
        else:
            return f'Coven member "{self.name}" did not drink blood today.'


    def sunrise(self):
        if self.in_coffin == False or self.drank_blood_today == False:
            __class__.coven.remove(self)
            return f'Coven member "{self.name}" is either not in their coffin, or did not drink blood in the last day so will be removed'

    @classmethod
    def sunset(cls):
        for i in cls.coven:
            drank_blood_today = False
            in_coffin = False
        return 'The entire coven is out in search of blood'


    def go_home(self):
        for i in __class__.coven:
            self.in_coffin = True
            return f'The vampire "{self.name} " is in their coffin.'


def main():
    Dracula = Vampire.create('Bethany', 1000,  False, True)
    Cullen = Vampire.create('Edward', 123, True, False)
    print(Dracula.go_home())
    print(Dracula.drink_blood())
    print(Vampire.sunset())



main()
