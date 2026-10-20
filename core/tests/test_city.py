from core.city.city import City

def test_spend_food():
    city = City()

    result = city.spend_food(100)

    assert result == "SUCCESS"
    assert city.get_food() == 200

def test_spend_food1():
    city = City()

    result = city.spend_food(400)

    assert result == "INSUFFICIENT_FOOD"
    assert city.get_food() == 300

    