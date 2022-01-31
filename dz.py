class Parking:
    TYPE_ORDINARY_CAR = 1
    TYPE_TRUCK_CAR = 2
    TYPE_MUNICIPAL_CAR = 3

    price_of_hour = 100
    coeff_for_municipal_car = 0.8

    def __init__(self, type_car, dimensions=None):
        if type_car not in [
            self.TYPE_ORDINARY_CAR,
            self.TYPE_TRUCK_CAR,
            self.TYPE_MUNICIPAL_CAR
        ]:
            raise ValueError("The type_car value is specified incorrectly!")

        if type_car == self.TYPE_TRUCK_CAR and not dimensions:
            raise ValueError("Dimensions for the truck are not specified!")

        if dimensions and type(dimensions) not in [int, float]:
            raise ValueError("Error value dimensions!")

        self.dimensions = dimensions
        self.type_car = type_car

    def get_price(self, hours):
        if type(hours) not in [int, float]:
            raise ValueError("Error value hours!")

        if type(self.price_of_hour) not in [int, float]:
            raise ValueError("Error value !")

        if type(self.coeff_for_municipal_car) not in [int, float]:
            raise ValueError("Error value coeff_for_municipal_car!")

        if hours <= 0:
            raise ValueError("The number of hours should be more null!")

        if self.price_of_hour <= 0:
            raise ValueError("The number of price_of_hour should be more null!")

        if self.coeff_for_municipal_car <= 0:
            raise ValueError("The number of coeff_for_municipal_car should be more null!")

        # ----------------------------------

        _text = "Price park: %f"
        if self.type_car == 1:
            print(_text % round((self.price_of_hour * hours)))

        elif self.type_car == 2:
            print(_text % round((self.price_of_hour * self.dimensions * hours)))

        elif self.type_car == 3:
            print(_text % round((self.price_of_hour * self.coeff_for_municipal_car * hours)))
