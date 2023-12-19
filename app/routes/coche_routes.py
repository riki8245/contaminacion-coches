from flask import Blueprint
from controller.coche_controller import CocheController

coche_routes = Blueprint("coche_routes", __name__)


@coche_routes.route('/')
def get_all():
    return CocheController.get_all()

@coche_routes.route('/create-many/', methods=['POST'])
def create_many():
    return coche_routes.create_many()

