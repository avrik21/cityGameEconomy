from core.city.city import City
import pytest

@pytest.mark.parametrize(
    "amount, expected_result, expected_food",
    [
        (100, "SUCCESS", 200),
        (300, "SUCCESS", 0),
        (400, "INSUFFICIENT_FOOD", 300),])
def test_spend_food(amount, expected_result, expected_food):
    city = City()

    result = city.spend_food(amount)
    assert result == expected_result
    assert city.get_food() == expected_food

@pytest.mark.parametrize(
    "amount, expected_result, expected_money",
    [
        (100, "SUCCESS", 1100),
        (-100, "NEGATIVE_AMOUNT", 1000),
        ("100", "NOT_INTEGER", 1000),])
def test_add_money(amount, expected_result, expected_money):
    city = City()

    result = city.add_money(amount)
    assert result == expected_result
    assert city.get_money() == expected_money

@pytest.mark.parametrize(
    "amount, expected_result, expected_citizens",
    [
        (100, "SUCCESS", 200),
        (-100, "NEGATIVE_AMOUNT", 100),
        ("100", "NOT_INTEGER", 100),])
def test_add_citizens(amount, expected_result, expected_citizens):
    city = City()

    result = city.add_citizens(amount)
    assert result == expected_result
    assert city.get_citizens() == expected_citizens

@pytest.mark.parametrize(
    "amount, expected_result, expected_citizens",
    [
        (10, "SUCCESS", 90),
        (100, "SUCCESS", 0),
        ("100", "NOT_INTEGER", 100),
        (110, "INSUFFICIENT_CITIZENS", 100),
        (-10, "LESS_ZERO", 100),])
def test_remove_citizens(amount, expected_result, expected_citizens):
    city = City()

    result = city.remove_citizens(amount)
    assert result == expected_result
    assert city.get_citizens() == expected_citizens

@pytest.mark.parametrize(
    "amount, expected_result, expected_food",
    [
        (100, "SUCCESS", 400),
        ("100", "NOT_INTEGER", 300),
        (-100, "NEGATIVE_AMOUNT", 300),
        (0, "NEGATIVE_AMOUNT", 300),
        ])
def test_add_food(amount, expected_result, expected_food):
    city = City()

    result = city.add_food(amount)
    assert result == expected_result
    assert city.get_food() == expected_food