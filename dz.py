
class Parking:
    TYPE_ORDINARY_CAR = 1
    TYPE_TRUCK_CAR = 2
    TYPE_MUNICIPAL_CAR = 3

    price_of_hour = 100

    def __init__(self, type_car):
        self.type_car = type_car

    def get_price(self, hours):
        if type(hours) not in [int, float]:
            raise ValueError("Error value hours!")

        _text = "Price park: %f"
        if self.type_car == 1:
            print("OK")

        elif self.type_car == 2:
            print("Not Found")

        elif self.type_car == 3:
            print(_text % round((self.price_of_hour * 0.8 * hours)))


park = Parking(Parking.TYPE_MUNICIPAL_CAR)
park.get_price(24)