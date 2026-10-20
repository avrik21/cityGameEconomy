from core.city.city import City
import pytest

@pytest.mark.parametrize(
    "amount, expected_result, expected_food",
    [
        (100, "SUCCESS", 200),
        (300, "SUCCESS", 0),
        (400, "INSUFFICIENT_FOOD", 300),
    ]
)

def test_spend_food(amount, expected_result, expected_food):
    city = City()

    result = city.spend_food(amount)
    assert result == expected_result
    assert city.get_food() == expected_food