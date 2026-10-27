from core.building.factory.factory import Factory
from core.building.factory.factory_manager import FactoryManager
from core.city.city import City

class TestFactory:
    def setup_method(self):
        self.city = City()
        self.factory_manager = FactoryManager(self.city)
        self.factory1 = Factory("factory", 1500, 50)
        self.city.add_building(self.factory1)

    def test_upgrade_factory(self):
        factory_id = self.factory1.get_id()

        level = 2
        raw_material = 15
        product_per_cycle = 30

        for i in range(1, 5):
            result = self.factory_manager.upgrade_factory(factory_id)

            assert result == "SUCCESS"
            assert self.factory_manager.get_factory(factory_id).get_level() == level
            assert self.factory_manager.get_factory(factory_id).get_raw_material() == raw_material
            assert self.factory_manager.get_factory(factory_id).get_product_per_cycle() == product_per_cycle
            level += 1
            raw_material += 5
            product_per_cycle += 10

    def test_max_level_factory(self):
        factory_id = self.factory1.get_id()
        self.factory_manager.upgrade_factory(factory_id)
        self.factory_manager.upgrade_factory(factory_id)
        self.factory_manager.upgrade_factory(factory_id)
        self.factory_manager.upgrade_factory(factory_id)
        result = self.factory_manager.upgrade_factory(factory_id)
        
        assert result == "MAX_LEVEL"
        assert self.factory_manager.get_factory(factory_id).get_level() == 5
        assert self.factory_manager.get_factory(factory_id).get_raw_material() == 30
        assert self.factory_manager.get_factory(factory_id).get_product_per_cycle() == 60

    def test_not_integer(self):
            result = self.factory_manager.upgrade_factory("2")
            assert result == "NOT_INTEGER"
    
    def test_invalid_id(self):
        result = self.factory_manager.upgrade_factory(-2)
        assert result == "INVALID_ID"

    def test_non_object(self):
        result = self.factory_manager.upgrade_factory(3)
        assert result == "NO_OBJECT"