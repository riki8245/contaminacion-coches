from flask import render_template
from flask import Blueprint

admin_routes = Blueprint("admin_routes", __name__)

@admin_routes.route('/')
def index():
    return render_template('index.html')
