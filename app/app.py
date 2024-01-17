from flask_cors import CORS
from flask import Flask, redirect
from config import config
from db.client import initialize_database, create_new_table, check_empty_table
from use_cases.coche import load_coches

# Routes
from routes.coche_routes import coche_routes
from routes.admin_routes import admin_routes

app = Flask(__name__)

# Es necesario para poder dejar acceder desde otros puertos
CORS(app)

def page_not_found(error):
    return "<h1>Not found page</h1>"

# Ruta predeterminada que redirige a /view
@app.route('/')
def index():
    return redirect('/view')

if __name__ == '__main__':
    app.config.from_object(config['development'])

    # Inicializar database
    initialize_database()
    create_new_table()

    # Blueprints
    app.register_blueprint(coche_routes, url_prefix='/car')
    app.register_blueprint(admin_routes, url_prefix='/view')
    

    if check_empty_table():
        load_coches()
    # Error handlers
    app.register_error_handler(404, page_not_found)
    app.run()
