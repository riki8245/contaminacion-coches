from domain.repositories.coche_repository import CocheRepository
from domain.entities.coche import Coche
import pandas as pd
from tqdm import tqdm

database = 'app/resources/huella-de-carbono-de-los-vehiculos-del-parque-movil.csv'

class LoadCoches:

    def __init__(self, coche_repository: CocheRepository):
        self._coche_repository: CocheRepository = coche_repository

    def execute(self):
        table = pd.read_csv(database)
        table.columns = table.columns.str.lower()
        # table.drop_duplicates(subset=['id'], inplace=True)
        list_of_coches = table.to_dict(orient='records')
        progress_bar = tqdm(total=len(list_of_coches), desc='Cargando base de datos:')
        count = 0
        for item in list_of_coches:
            coche = Coche(**item)
            try:
                self._coche_repository.create_coche(coche)
                count += 1
            except:
                print('Número de registros cargados: ', count)
            progress_bar.update(1)
        print('Tabla de datos cargada exitosamente')
