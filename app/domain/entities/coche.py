class Coche:
    def __init__(self, id=None, ano=None, mes=None, marca=None, modelo=None, tipovehiculo=None,
                 km_mes=None, grco2_km=None, grco2=None) -> None:
        self.id = id
        self.ano = ano
        self.mes = mes
        self.marca = marca
        self.modelo = modelo
        self.tipovehiculo = tipovehiculo
        self.km_mes = km_mes
        self.grco2_km = grco2_km
        self.grco2 = grco2
        self.label = ("A" if grco2_km <= 95 else "B" if grco2_km <= 120 else "C") if grco2_km else None

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get('id'),
            ano=data.get('ano'),
            mes=data.get('mes'),
            marca=data.get('marca'),
            modelo=data.get('modelo'),
            tipovehiculo=data.get('tipovehiculo'),
            km_mes=data.get('km_mes'),
            grco2_km=data.get('grco2_km'),
            grco2=data.get('grco2'),
            label=data.get('label') #Quiza corregir
        )

    def to_dict(self):
        return {
            'id': self.id,
            'ano': self.ano,
            'mes': self.mes,
            'marca': self.marca,
            'modelo': self.modelo,
            'tipovehiculo': self.tipovehiculo,
            'km_mes': self.km_mes,
            'grco2_km': self.grco2_km,
            'grco2': self.grco2,
            'label': self.label
        }

    def headers(self):
        return [
            key.lower() for key in self.__dict__.keys()
            if not key.startswith("_")
        ]

    @staticmethod
    def list_to_json(values):
        coche = Coche()
        coche.id = values[0]
        coche.ano = values[1]
        coche.mes = values[2]
        coche.marca = values[3]
        coche.modelo = values[4]
        coche.tipovehiculo = values[5]
        coche.km_mes = values[6]
        coche.grco2_km = values[7]
        coche.grco2 = values[8]
        coche.label = ("A" if coche.grco2_km <= 95 else "B" if coche.grco2_km <= 120 else "C") if coche.grco2_km else None
        return coche

    def update_coche(self, item):
        # Update attributes with values from 'item' if provided, otherwise retain existing values
        self.id = item.id if item.id else self.id
        self.ano = item.ano if item.ano else self.ano
        self.mes = item.mes if item.mes else self.mes
        self.marca = item.marca if item.marca else self.marca
        self.modelo = item.modelo if item.modelo else self.modelo
        self.tipovehiculo = item.tipovehiculo if item.tipovehiculo else self.tipovehiculo
        self.km_mes = item.km_mes if item.km_mes else self.km_mes
        self.grco2_km = item.grco2_km if item.grco2_km else self.grco2_km
        self.grco2 = item.grco2 if item.grco2 else self.grco2
        self.label = ("A" if item.grco2_km <= 95 else "B" if item.grco2_km <= 120 else "C") if item.grco2_km else self.label
        

        return self
