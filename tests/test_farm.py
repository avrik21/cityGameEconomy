from core.building.farm.farm_manager import FarmManager
from core.building.farm.farm import Farm
from core.city.city import City
import pytest

class TestFarm:
    def setup_method(self):
        self.city = City()
        self.farm_manager = FarmManager(self.city)

        farm1 = Farm("farm", 1000, 100)
        farm2 = Farm("farm", 1000, 100)
        self.city.add_building(farm1)
        self.city.add_building(farm2)
    
    @pytest.mark.parametrize(
        "amount, expected_result, expected_lvl, expected_food_per_cycle",
        [
            (1, "SUCCESS", 2, 150),
            (1, "SUCCESS", 3, 200),
            (2, "SUCCESS", 2, 150),
            
        ])
    def test_upgrade_farm(self, amount, expected_result, expected_lvl, expected_food_per_cycle):
        result = self.farm_manager.upgrade_farm(amount)

        assert result == expected_result
        assert self.farm_manager.get_farm(amount).get_level() == expected_lvl
        assert self.farm_manager.get_farm(amount).get_food_per_cycle() == expected_food_per_cycle       