from controller.base_controller import BaseController
from flask import jsonify, request

# import use cases
from use_cases.coche import get_all_coches, create_coche

class CocheController(BaseController):
        
    @staticmethod
    def get_all():
        try:
            params = request.args
            data = get_all_coches(params)

            response = {
                "count": len(data),
                "coche": [coche.to_dict() for coche in data],
            }

            return response
        except Exception as ex:
                    return jsonify({'Error message': str(ex)}), 500
        
    @staticmethod
    def create():
        try:
            json = request.json
            return create_coche(json)
        except Exception as ex:
                    return jsonify({'Error message': str(ex)}), 500
        
        
    @staticmethod
    def create_many():
        try:
            json = request.json
            count = 0
            response = []
            for coche in json:
                response.append(create_coche(coche))
                count += 1

            return {
                "count": count,
                "coche": response,
            }
        
        except Exception as ex:
                    return jsonify({'Error message': str(ex)}), 500