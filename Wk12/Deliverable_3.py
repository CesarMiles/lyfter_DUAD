#Pokemon class types that can be given to multiple pokemons at once. i.e Laprass being Ice and Water type
class Water():
    def water_strenght(self):
        print(f'Damage to fire type +10')
        print(f'Damage to earth type +10')
        print(f'Damage to rock type +10')

    def water_weakness(self):
        print(f'Damage taken from plant type +10')
        print(f'Damage taken from +10')

class Ice():
    def ice_strenght(self):
        print(f'Damage to flying type +10')
        print(f'Damage to dragon type +10')
    
    def ice_weakness(self):
        print(f'Damage taken from fighting type +10')
        print(f'Damage taken from metal type +10')


class Laprass(Water, Ice):
    pass

laprass = Laprass()

laprass.ice_strenght()
laprass.water_strenght()