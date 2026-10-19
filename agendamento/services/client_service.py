from flask_jwt_extended import create_access_token
from database.models import Usuario, Funcionarios

import re 

# VALIDAÇÃO USUARIOS 

def validar_usuario(dados):
    campos_obrigatorios = ["nome", "email", "telefone", "senha"]
    
    for campo in campos_obrigatorios:
        if not dados.get(campo):
            # Corrigido o '0' para 'O' aqui em baixo:
            raise ValueError(f"O campo '{campo}' é obrigatório e não pode estar vazio.")


    nome = dados.get("nome").strip()
    email = dados.get("email")
    tel = dados.get("tel")
    senha = dados.get("senha")

    if len(nome) > 200:
        raise ValueError(f"Error: Caracteres máximo permito é até 200.")

    # Email
    padrao_email = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    
    if not re.match(padrao_email, email):
        raise ValueError("O formato do e-mail é inválido. Verifique se digitou corretamente.")

    # Telefone
    telefone_limpo = re.sub(r'\D', '', tel)
    if len(telefone_limpo) not in [10, 11]:
        raise ValueError("O telefone deve conter 10 ou 11 dígitos (com DDD).")

    novo_usuario = Usuario(nome=nome, email=email, senha_hash=senha)

    return True


