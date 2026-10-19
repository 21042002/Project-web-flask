from ext.app_extensions import db, bcrypt
import uuid


class Usuario(db.Model):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    nome  = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    telefone = db.Column(db.String(20), nullable=True)
    senha_hash = db.Column(db.String(200), nullable=False)

    def __init__(self, nome, email, telefone, senha):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.senha_hash = bcrypt.generate_password_hash(senha).decode('utf-8')

    def __repr__(self):
        return f"<Usuario {self.email}>"

    # Criação de usuário
    def salvar(self):
        db.session.add(self)
        db.session.commit()

        
class Funcionarios(db.Model):
    __tablename__ = "funcionarios"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=True)
    email = db.Column(db.String(100), unique=True, nullable=True)
    senha = db.Column(db.String(200), nullable=True)

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha_hash = bcrypt.generate_password_hash(senha).decode('utf-8')


    def __repr__(self):
        return f"Usario {self.nome}"

    # Criação de funcionário
    def salvar(self):
        db.session.add(self)
        db.session.commit()
