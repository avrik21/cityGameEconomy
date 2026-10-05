from core.building.factory.factory import Factory

class FactoryManager:
    def __init__(self, city):
        self.city = city

    def upgrade_factory(self, factory_id):
        if not isinstance(factory_id, int):
            return "NOT_INTEGER" 
        if factory_id < 0:
            return "INVALID_ID"

        for item in self.city.get_buildings():
            if isinstance(item, Factory) and item.get_id() == factory_id:
                result = item.upgrade_factory()
                if result == "SUCCESS":
                    return "SUCCESS"
                return "MAX_LEVEL"
        return "NO_OBJECT"