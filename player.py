class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100

    def take_damage(self, amount):
        self.hp -= amount
        print(f"체력이 {self.hp} 남았습니다.")

    def take_damage(self, amount):
        self.hp -= amount
        print(f"체력이 {self.hp} 남았습니다.")