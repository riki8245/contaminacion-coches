from domain.entities.coche import Coche
from domain.repositories.coche_repository import CocheRepository

class CreateCoche:

    def __init__(self, coche_repository: CocheRepository):
        self._coche_repository: CocheRepository = coche_repository

    def execute(self, coche_data):
        coche = Coche(**coche_data)
        result = self._coche_repository.create_coche(coche)
        return result