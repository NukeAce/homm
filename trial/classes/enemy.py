class Enemy:
    def __init__(self, hp,mp):
        self.max_hp=mp
        self.hp=hp
        self.max_mp=mp
        self.mp=mp

    def gethp(self):
        return self.max_hp
