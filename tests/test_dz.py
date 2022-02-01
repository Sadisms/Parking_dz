from main import Parking
import pytest


def test_parking_class():
    assert Parking(Parking.TYPE_ORDINARY_CAR).get_price(1) == 100

    assert Parking(Parking.TYPE_TRUCK_CAR, 10).get_price(1) == 1000

    assert Parking(Parking.TYPE_MUNICIPAL_CAR).get_price(1) == 80

    with pytest.raises(ValueError):
        Parking(0)

    with pytest.raises(ValueError):
        Parking(Parking.TYPE_TRUCK_CAR).get_price(1)

    with pytest.raises(ValueError):
        Parking(Parking.TYPE_ORDINARY_CAR).get_price(0)

    with pytest.raises(TypeError):
        Parking(Parking.TYPE_ORDINARY_CAR).get_price('1')

    park = Parking(1)

    with pytest.raises(ValueError):
        park.coeff_for_municipal_car = 0
        park.get_price(1)

    with pytest.raises(TypeError):
        park.price_of_hour = '0'
        park.get_price(1)

