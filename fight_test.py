class Hero:
    def __init__(self):
        self.health = 20
        self.attack = 1
        self.items = []

class Rodent:
    def __init__(self):
        self.health = 2
        self.attack = 1

def attack_sequence(attacker, defender):
    print('Encounter occurs')
    print('Attacker Health / Damage:', attacker.health, '/', attacker.attack)
    print('Defender Health / Damage:', defender.health, '/', defender.attack)
    print('\n')
    while(defender.health > 0 and attacker.health > 0):
        # Defender takes damage from attacker
        defender.health = defender.health - attacker.attack
        # Output damage
        print('Defender takes', attacker.attack, 'damage.')
        print('Defender is at', defender.health, 'health.\n')
        # Attacker takes damage from defender
        attacker.health = attacker.health - defender.attack
        print('Attacker takes', defender.attack, 'damage.')
        print('Attacker is at', attacker.health, 'health.\n')
    if(attacker.health <= 0):
        print('Attacker has died.')
    else:
        print('Defender has died.')

knight = Hero()
rat = Rodent()

attack_sequence(knight, rat)

print('After the fight, your health is', knight.health)
