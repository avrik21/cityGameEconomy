from core.building.farm.farm import Farm
from core.city.city import city
from core.building.farm.farm_manager import farm_manager

farm1 = Farm("farm", 1000, 100)
farm2 = Farm("farm", 1000, 100)
farm3 = Farm("farm", 1000, 100)
farm4 = Farm("farm", 1000, 100)

city.add_building(farm1)
city.add_building(farm2)
city.add_building(farm3)
city.add_building(farm4)

farm_manager.upgrade_farm(1)

print(city.get_buildings()[0].__dict__)
print(city.get_buildings()[1].__dict__)