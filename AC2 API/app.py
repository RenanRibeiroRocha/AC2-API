from flask import Flask, render_template, redirect, request, flash


app = Flask(__name__)
app.config['SECRET_KEY'] = 'teste@123'



@app.route('/')
def home():
    return render_template('login.html')



@app.route('/login', methods=['POST'])
def login():

    nome = request.form.get('nome')
    senha = request.form.get('senha')

    if nome == 'usuario.teste' and senha == 'teste@123':
        return render_template("home.html")
    else:
        return render_template("login.html")
    


if __name__ in "__main__":
    app.run(debug=True)    