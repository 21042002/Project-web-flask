from flask import Flask
from dotenv import load_dotenv 
import os 

# importando as extensões 
from ext.app_extensions import db, bcrypt, jwt
from config.config import configure_jwt

load_dotenv()

PORT = int(os.getenv("PORT"))

def create_app():
    app = Flask(__name__)

    #  Configurações:
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = os.getenv("SECRET_KEY")

    # Inicialização das extensões
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    # Configuração do JWT
    configure_jwt(jwt, app)

    # Registro de rotas:

    #  Criação de Banco e tabelas
    with app.app_context():
        import database.models
        db.create_all()

    return app

app = create_app()

if __name__ == "__main__":
    print(f"Servido rodando na porta: {PORT}")
    app.run(port=PORT, debug=True)