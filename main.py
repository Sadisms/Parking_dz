from typing import Union


class Parking:
    TYPE_ORDINARY_CAR = 1
    TYPE_TRUCK_CAR = 2
    TYPE_MUNICIPAL_CAR = 3

    price_of_hour = 100
    coeff_for_municipal_car = 0.8

    def __init__(self, type_car: int, dimensions: Union[int, float, None] = None, **kwargs):
        """
        Calculation of parking costs for car types
        Args:
            :param type_car: type car waited data TYPE_ORDINARY_CAR, TYPE_TRUCK_CAR, TYPE_MUNICIPAL_CAR
            :param dimensions: dimensions of a car for a truck car type
            :param kwargs: other parameters

        Raises:
            ValueError: the type_car value is specified incorrectly
            ValueError: dimensions for the truck are not specified
            TypeError: error value dimensions
            ValueError: the number of dimensions should be more null
        """
        if type_car not in [
            self.TYPE_ORDINARY_CAR,
            self.TYPE_TRUCK_CAR,
            self.TYPE_MUNICIPAL_CAR
        ]:
            raise ValueError("The type_car value is specified incorrectly!")

        if type_car == self.TYPE_TRUCK_CAR and not dimensions:
            raise ValueError("Dimensions for the truck are not specified!")

        if dimensions and type(dimensions) not in [int, float]:
            raise TypeError("Error value dimensions!")

        if type_car == self.TYPE_TRUCK_CAR and dimensions <= 0:
            raise ValueError("The number of dimensions should be more null!")

        self.dimensions = dimensions
        self.type_car = type_car

    def get_price(self, hours: Union[int, float], **kwargs) -> float:
        """
        Get the cost of parking
        Args:
            :param hours: number of parking hours
            :param kwargs: other parameters

        Raises:
            TypeError: error value (hours/price_of_hour/coeff_for_municipal_car)
            ValueError: the number of (hours/price_of_hour/coeff_for_municipal_car) should be more null

        Returns:
            :return: the cost of parking
        """
        for v in [hours, self.price_of_hour, self.coeff_for_municipal_car]:
            if type(v) not in [int, float]:
                raise TypeError(f"Error value {v}!")

            if v <= 0:
                raise ValueError(f"The number of {v} should be more null!")

        if self.type_car == self.TYPE_ORDINARY_CAR:
            return round((self.price_of_hour * hours))

        elif self.type_car == self.TYPE_TRUCK_CAR:
            return round((self.price_of_hour * self.dimensions * hours))

        elif self.type_car == self.TYPE_MUNICIPAL_CAR:
            return round((self.price_of_hour * self.coeff_for_municipal_car * hours))