from flask import Flask, redirect, request, render_template

app = Flask(__name__)

funcionarios = []

@app.route("/", methods=['GET','POST'])
def index():
    if request.method == "POST":

        nome = request.form.get("nome").strip()
        idade = request.form.get("idade")
        telefone = request.form.get("telefone")

        try:
            idade = int(idade)

            if len(nome) < 10 and '' not in nome:
                return 'Erro: Nome tem que ser completo'
            elif idade < 18:
                return 'Erro: Menor de idade, não permitido cadastro'
            
        except (ValueError, TypeError, AttributeError):
            return 'Erro de codigo'


        funcionarios.append({
            "nome": nome,
            "idade": idade,
            "telefone": telefone
        })

        return redirect('cadastro')

    return render_template('index.html', funcionarios=funcionarios)


# Rota Listar dados
@app.route('/cadastro')
def mostrar_funcionarios():

    return render_template('Cadastro.html', funcionarios=funcionarios)


if __name__ == "__main__":
    app.run(debug=True)