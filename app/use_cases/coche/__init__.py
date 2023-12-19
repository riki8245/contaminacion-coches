# Use cases package
from use_cases.coche.load_coches import LoadCoches
from use_cases.coche.create_coche import CreateCoche
from use_cases.coche.get_all_coches import GetAllCoches

# Repos
from domain.repositories.coche_repository import CocheRepository

_info_repo = CocheRepository()

# Use cases
get_all_coches = GetAllCoches(_info_repo).execute
create_coche = CreateCoche(_info_repo).execute
load_coches = LoadCoches(_info_repo).execute