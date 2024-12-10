class Country:
    def __init__(self):
        self.name = "나라이름"
        self.population = "인구"
        self.capital = "수도"

    def show(self):
        print("국가 클래스의 메소드")

class Korea(Country):
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print("국가 이름:", self.name)

country = Korea("대한민국")
country.show()
print(country.name)
country.show_name()