from abc import ABC, abstractmethod


class Creature:
    def __init__(self, attack, health):
        self.attack = attack
        self.health = health
        self.initial_health = health


class CardGame(ABC):
    def __init__(self, creatures):
        self.creatures = creatures

    def combat(self, c1_index, c2_index):
        c1 = self.creatures[c1_index]
        c2 = self.creatures[c2_index]

        alive1 = self.hit(c2, c1)
        alive2 = self.hit(c1, c2)

        if alive1 == alive2:
            return -1

        return c1_index if alive1 else c2_index

    @abstractmethod
    def hit(self, attacker, defender):
        pass


class TemporaryDamageCardGame(CardGame):
    def hit(self, attacker, defender):
        if defender.health - attacker.attack <= 0:
            defender.health = 0
            return False

        defender.health = defender.initial_health
        return True


class PermanentDamageCardGame(CardGame):
    def hit(self, attacker, defender):
        defender.health -= attacker.attack
        defender.initial_health = defender.health

        return defender.health > 0


if __name__ == '__main__':
    creatures_list = [Creature(1, 2), Creature(1, 3)]
    game = TemporaryDamageCardGame(creatures_list)
    print(game.combat(0, 1))

    creatures_list2 = [Creature(1, 2), Creature(1, 3)]
    game_p = PermanentDamageCardGame(creatures_list2)
    print(game_p.combat(0, 1))
    print(game_p.combat(0, 1))

    creatures_list3 = [Creature(2, 2), Creature(2, 2)]
    game_p2 = PermanentDamageCardGame(creatures_list3)
    print(game_p2.combat(0, 1))