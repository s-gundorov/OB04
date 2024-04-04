class Weapon:
    def attack(self):
        raise NotImplementedError("Вам нужно реализовать этот метод.")

class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом."

class Bow(Weapon):
    def attack(self):
        return "Боец наносит удар из лука."

class Fighter:
    def __init__(self):
        self.weapon = None

    def change_weapon(self, weapon):
        self.weapon = weapon

    def fight(self):
        if not self.weapon:
            return "Боец не вооружен."
        return self.weapon.attack()

class Monster:
    pass

# Демонстрация игры
fighter = Fighter()
monster = Monster()

# Боец выбирает меч.
sword = Sword()
fighter.change_weapon(sword)
print(fighter.fight())  # Боец наносит удар мечом.

# Боец выбирает лук.
bow = Bow()
fighter.change_weapon(bow)
print(fighter.fight())  # Боец наносит удар из лука.