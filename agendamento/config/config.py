from datetime import timedelta

def configure_jwt(jwt_manager, app):

    # Configura o tempo de expiração, callbacks de erro e segurança do JWT;

    # Defindo o tempo de expiração
    app.config["JWT_ACESS_TOKEN_EXPRIES"] = timedelta(minutes=15)


    @jwt_manager.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return {"erro": "O seu token JWT expirou. Por favor, faça login novamente."}, 401

    @jwt_manager.invalid_token_loader
    def invalid_token_callback(error):
        return {"erro": "Token inválido ou corrompido."}, 401

    @jwt_manager.unauthorized_loader
    def missing_token_callback(error):
        return {"erro": "Acesso negado. Nenhum token de autenticação foi fornecido."}, 401




