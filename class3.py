class God():
    def __init__(self, name, age, country, height):
        self.name = name
        self.age = age
        self.country = country
        self.height = height
    def introduce(self):
        print(f"저는 {self.name}이고, 나이는 {self.age}세 입니다. {self.country}나라에서 태어났고, 키는 {self.height}cm 입니다.")

a = God('김현우', 20, '아르헨티나', 180)
b = God('요시무라', 80, '일본', 170)
c = God('세바스찬', 10, '프랑스', 130)
d = God('제임스', 11, '영국', 171)
e = God('왕', 33, '중국', 145)

c.introduce()
a.introduce()