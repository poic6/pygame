class Fighter():
    def __init__(self, model, missile):
        self.model = model
        self.missile = missile
    def attack(self):
        print(self.model+" 출격!")
    def fire(self):
        print(self.missile+" 발사!")

fighter1 = Fighter('김현우', '미사일')
fighter1.attack()
fighter1.fire()
fighter2 = Fighter('박현우', 'ICBM')
fighter2.fire()