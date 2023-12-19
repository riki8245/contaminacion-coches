from utils.uuii import UniqueId
from db.driver import psql_driver
from domain.entities.coche import Coche

COLLECTION_NAME = 'coches'

class CocheRepository:
    
    def __init__(self):
        self.driver = psql_driver()

    def get_all_coches(self,filters):
        coches_data = self.driver.get_all(COLLECTION_NAME, self.filterMap(filters))
        if coches_data is not None:
            return [Coche.list_to_json(coche_data) for coche_data in coches_data]
        else:
            return []
        
    def create_coche(self, coche):
        coche_data = coche.to_dict()
        if coche_data['id']== None:
            coche_data['id'] = UniqueId.get_uuid()
        numberSong = self.driver.create(COLLECTION_NAME, coche_data.keys(), list(coche_data.values()))
        response = {
            "coche" : coche_data,
            "count": numberSong,
        }
        return response
    
    def filterMap(self, itemArray):
        mapFilter = []
        for item in itemArray:
            if itemArray[item] is not None:
                mapFilter.append(f"{item} ILIKE '%{itemArray[item]}%'")

        condition = ' AND '.join(mapFilter)
        return condition