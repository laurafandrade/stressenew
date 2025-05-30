from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Login Simples
USUARIO = "admin"
SENHA = "1234"

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def do_login():
    username = request.form['username']
    password = request.form['password']
    if username == USUARIO and password == SENHA:
        return redirect('/painel')
    else:
        return "❌ Usuário ou senha inválidos."

@app.route('/painel')
def painel():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
