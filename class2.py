class Hello():
    def __init__(self, name):
        self.name = name
    def greeting(self):
        print(self.name+" 안녕하세요?")
    def goodbye(self):
        print("안녕히가세요!")

a = Hello('홍길동')
a.greeting()
a.goodbye()
b = Hello('유관순')
c = Hello('윤석열')
c.greeting()
