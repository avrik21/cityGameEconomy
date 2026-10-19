from core.building.farm.farm import Farm
from core.building.factory.factory import Factory
from core.city.city import City
from core.building.farm.farm_manager import FarmManager
from core.building.factory.factory_manager import FactoryManager
from core.product_manager import ProductManager

city = City()
farm_manager = FarmManager(city)
factory_manager = FactoryManager(city)
product_manager = ProductManager(city)

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

farm_manager.upgrade_farm(1)

print(city.get_food())

product_manager.add_food()

print(city.get_food())

for i in city.get_buildings():
    print(i.__dict__)