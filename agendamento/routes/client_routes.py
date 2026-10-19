from flask import blueprints, request, jsonify
from services.client_service import validar_usuario

auth_bp = blueprints("auth", __name__)

@auth_bp.route('/login', methods=["POST"])
def login():
    dados = request.get_json()

    nome = dados.get("nome")


@auth_bp.route("/registrer", methods=['POST'])
def register():
    dados = request.get_json()
    
    try:
        validar_usuario(dados)
        return jsonify({ "message": "Usuário criado com sucesso" }), 201

    except ValueError as e:
        print("Erro:", str(e))
        return jsonify({"erro": "Servidor não conseguiu processar a informaçao. "}), 400

    