# Importação de bibliotecas
from flask import Flask, render_template
from routes import bp1

# Criação do aplicativo Flask que vai ser responsável por subir a aplicação em Web.
app = Flask(__name__)

# Linkagem do arquivo routes.py para poder acessar a rota do backend.
app.register_blueprint(bp1)

# Declaração da rota principal que vai chamar o arquivo de home.html assim que subir a aplicação.
@app.route("/")
def home():
    return render_template("home.html")

if __name__ == '__main__':
    app.run(debug=False)

# Para rodar o programa localmente basta ter o Python instalado 
# e instalar as dependencias, na sequência, abrir um CMD na pasta do projeto
# e digitar "python app.py", irá abrir um servidor em determinado endereço informado 
# no CMD.