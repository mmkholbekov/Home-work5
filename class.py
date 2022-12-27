
class Hero:
    def __init__(self,name,abyliti):
        self.name = name
        self.abyliti = abyliti

class Hero_super(Hero):

    def __str__(self):
        return f"{self.name}"

    def new(self):
        print('it is super_hero')












