from flask import Flask
import os

# instanciar o flask
app = Flask(__name__)

#carregar uma variavel de ambiente
service_name = os.environ.get("SERVICE_NAME")
if not service_name:
    service_name = 'Servico 3'

#criar uma rota
@app.route('/')
def main():
    return service_name

#rodar a app
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")