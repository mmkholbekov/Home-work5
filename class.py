
class Hero:
    def __init__(self,name,abyliti):
        self.name = name
        self.abyliti = abyliti

class Hero_super(Hero):
    def new(self):
        print(f'{self.name}')
    def no(self):
        print('it is super_hero')

    def __str__(self):
        return f'{self.name} {self.abyliti}'

x = Hero_super('Adam', 'fly')
x.new()
x.no()
print(x)











