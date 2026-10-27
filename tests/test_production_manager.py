from core.building.farm.farm import Farm
from core.building.factory.factory import Factory
from core.production_manager import ProductionManager
from core.city.city import City

class TestProductionManager:
    def setup_method(self):
        self.city = City()
        self.production_manager = ProductionManager(self.city)

    def test_add_food_success(self):
        farm1 = Farm()
        self.city.add_building(farm1)
        result = self.production_manager.add_food()
        assert result == "SUCCESS"
        assert self.city.get_food() == 350

    def test_add_food_nofarm(self):
        factory1 = Factory()
        self.city.add_building(factory1)
        result = self.production_manager.add_food()
        assert result == "NO_FARM"
        assert self.city.get_food() == 300
        
    def test_add_food_empty(self):
        result = self.production_manager.add_food()
        assert result == "EMPTY"
        assert self.city.get_food() == 300