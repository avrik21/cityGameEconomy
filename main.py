from core.building.farm.farm import Farm
from core.building.factory.factory import Factory
from core.city.city import City
from core.building.farm.farm_manager import FarmManager
from core.building.factory.factory_manager import FactoryManager

city = City()
farm_manager = FarmManager(city)
factory_manager = FactoryManager(city)

farm1 = Farm("farm", 1000, 100)
farm2 = Farm("farm", 1000, 100)
farm3 = Farm("farm", 1000, 100)
farm4 = Farm("farm", 1000, 100)

factory1 = Factory("factory", 1500, 50)
factory2 = Factory("factory", 1500, 50)
factory3 = Factory("factory", 1500, 50)
factory4 = Factory("factory", 1500, 50)

city.add_building(farm1)
city.add_building(farm2)
city.add_building(farm3)
city.add_building(farm4)

city.add_building(factory1)
city.add_building(factory2)
city.add_building(factory3)
city.add_building(factory4)

print(farm_manager.upgrade_farm(1))
print(farm_manager.upgrade_farm(1))
print(farm_manager.upgrade_farm(1))
print(farm_manager.upgrade_farm(1))
print(farm_manager.upgrade_farm(1))

print(factory_manager.upgrade_factory(5))
print(factory_manager.upgrade_factory(6))
print(factory_manager.upgrade_factory(7))
print(factory_manager.upgrade_factory(8))
print(factory_manager.upgrade_factory(8))


print(factory_manager.upgrade_factory(999))
print(factory_manager.upgrade_factory(-999))
print(factory_manager.upgrade_factory("1"))

print(farm_manager.upgrade_farm(999))
print(farm_manager.upgrade_farm(-999))
print(farm_manager.upgrade_farm("1"))

for i in city.get_buildings():
    print(i.__dict__)