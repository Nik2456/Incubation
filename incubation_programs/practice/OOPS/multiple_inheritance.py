class Brand:
    def __init__(self, brand):
        self.brand_name = brand

    def show_brand(self):
        print("Car brand is =", self.brand_name)


class Car:
    def __init__(self, car_name):
        self.car_name_value = car_name

    def show_car_name(self):
        print("Car name is =", self.car_name_value)


class Model(Brand, Car):
    def __init__(self, brand, car_name, series):
        Brand.__init__(self, brand)
        Car.__init__(self, car_name)
        self.series = series

    def car_model(self):
        print("Brand =", self.brand_name,
              "Car name =", self.car_name_value,
              "Car_model =", self.series)


m1 = Model("TATA", "Nexon", "Topend")
m1.show_brand()
m1.show_car_name()
m1.car_model()
