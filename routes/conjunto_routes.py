# routes/user_routes.py
from flask import Blueprint
from controllers.conjunto_controller import insert_conjunto_controller, obtener_conjuntos, total_conjuntos

conjunto_bp = Blueprint('conjunto_bp', __name__)

# Ajuste: no se deben ejecutar funciones en la definición de rutas
conjunto_bp.route('/insertConjunto', methods=['POST'])(insert_conjunto_controller)
conjunto_bp.route('/conjuntos/<int:id_usuario>', methods=['GET'])(obtener_conjuntos)
conjunto_bp.route('/conjuntos/total', methods=['GET'])(total_conjuntos)



