from domain.repositories.coche_repository import CocheRepository

class GetAllCoches:

    def __init__(self, coche_repository: CocheRepository):
        self._coche_repository: CocheRepository = coche_repository

    def execute(self,filters):
        coches = self._coche_repository.get_all_coches(filters)
        return coches
