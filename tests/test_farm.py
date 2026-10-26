from core.building.farm.farm_manager import FarmManager
from core.building.farm.farm import Farm
from core.city.city import City
import pytest

city = City()
farm1 = Farm("farm", 1000, 100)
farm2 = Farm("farm", 1000, 100)
city.add_building(farm1)
city.add_building(farm2)

class TestFarm:
    def setup_method(self):
        self.farm_manager = FarmManager(city)
    
    @pytest.mark.parametrize(
        "farm_id, expected_result, expected_lvl, expected_food_per_cycle",
        [
            (1, "SUCCESS", 2, 100),
            (1, "SUCCESS", 3, 150),
            (1, "SUCCESS", 4, 200),
            (1, "SUCCESS", 5, 250),
            (1, "MAX_LEVEL", 5, 250),
            (2, "SUCCESS", 2, 100),          
            (3, "NO_OBJECT", 2, 100),          
            ("3", "NOT_INTEGER", 2, 100),          
            (-1, "INVALID_ID", 2, 100),          
            
        ])
    def test_upgrade_farm(self, farm_id, expected_result, expected_lvl, expected_food_per_cycle):
        result = self.farm_manager.upgrade_farm(farm_id)
        
        assert result == expected_result
        if result not in ("NO_OBJECT", "NOT_INTEGER", "INVALID_ID"):
            assert self.farm_manager.get_farm(farm_id).get_level() == expected_lvl
            assert self.farm_manager.get_farm(farm_id).get_food_per_cycle() == expected_food_per_cycle       