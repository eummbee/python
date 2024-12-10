class Supermarket:
    count = 0
    def __init__(self,location,name,product,customer):
        self.location = location
        self.name = name
        self.product = product
        self.customer = customer
        Supermarket.count += 1
    
    def print_location(self):
        print(self.location)

    def change_category(self,change):
        self.product = change
        print(self.product)

    def show_list(self):
        print(self.product)

    def enter_customer(self):
        self.customer += 1

    def show_info(self):
        print(f"가게이름:{self.name}\n위치:{self.location}\n파는물건:{self.product}\n손님수:{self.customer}")
    
    def show_supermarket_count(self):
        print(Supermarket.count)

a = Supermarket("서울","이마트","사과, 배", 2)
b = Supermarket("대구","하나로마트","고기",1)

a.print_location()
a.change_category("포도")
a.show_list()
a.enter_customer()
a.show_info()
a.show_supermarket_count()



