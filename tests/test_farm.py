from core.building.farm.farm_manager import FarmManager
from core.building.farm.farm import Farm
from core.city.city import City

class TestFarm:
    def setup_method(self):
        self.city = City()
        self.farm_manager = FarmManager(self.city)
        self.farm1 = Farm("farm", 1000, 100)
        self.city.add_building(self.farm1)

    def test_upgrade_farm(self):
        farm_id = self.farm1.get_id()
        
        result = self.farm_manager.upgrade_farm(farm_id)
        
        assert result == "SUCCESS"
        assert self.farm_manager.get_farm(farm_id).get_level() == 2
        assert self.farm_manager.get_farm(farm_id).get_food_per_cycle() == 100       

        result = self.farm_manager.upgrade_farm(farm_id)
        
        assert result == "SUCCESS"
        assert self.farm_manager.get_farm(farm_id).get_level() == 3
        assert self.farm_manager.get_farm(farm_id).get_food_per_cycle() == 150       

        result = self.farm_manager.upgrade_farm(farm_id)
        
        assert result == "SUCCESS"
        assert self.farm_manager.get_farm(farm_id).get_level() == 4
        assert self.farm_manager.get_farm(farm_id).get_food_per_cycle() == 200       

        result = self.farm_manager.upgrade_farm(farm_id)
        
        assert result == "SUCCESS"
        assert self.farm_manager.get_farm(farm_id).get_level() == 5
        assert self.farm_manager.get_farm(farm_id).get_food_per_cycle() == 250       

        result = self.farm_manager.upgrade_farm(farm_id)
        
        assert result == "MAX_LEVEL"
        assert self.farm_manager.get_farm(farm_id).get_level() == 5
        assert self.farm_manager.get_farm(farm_id).get_food_per_cycle() == 250       

    def test_max_level(self):
        farm_id = self.farm1.get_id()
        self.farm_manager.upgrade_farm(farm_id)
        self.farm_manager.upgrade_farm(farm_id)
        self.farm_manager.upgrade_farm(farm_id)
        self.farm_manager.upgrade_farm(farm_id)
        result = self.farm_manager.upgrade_farm(farm_id)

        assert result == "MAX_LEVEL"
        assert self.farm_manager.get_farm(farm_id).get_level() == 5
        assert self.farm_manager.get_farm(farm_id).get_food_per_cycle() == 250  

    def test_not_integer(self):
        result = self.farm_manager.upgrade_farm("2")
        assert result == "NOT_INTEGER"

    def test_invalid_id(self):
        result = self.farm_manager.upgrade_farm(-2)
        assert result == "INVALID_ID"

    def test_non_object(self):
        farm_id = self.farm1.get_id()
        result = self.farm_manager.upgrade_farm(farm_id + 5)
        assert result == "NO_OBJECT"