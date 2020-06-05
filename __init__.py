import re

from flask import Flask, escape, request,render_template

app = Flask(__name__)

usuario = 'ubuntu'
projeto = 'deployflask'
git = 'https://github.com/Aguape21/deployflask.git'
enderecos = 'deployflask.e-li.me\ndeployflask2.e-li.me'

@app.route('/', )
def comeco():

    global usuario, projeto, git, enderecos

    return render_template("comeco.html",
                           usuario=usuario,
                           projeto=projeto,
                           git=git,
                           enderecos=enderecos)

@app.route('/tutorial', methods=['GET', 'POST'])
def tutorial():

    global usuario, projeto, git, enderecos

    if request.method == 'POST':
        form = request.form.to_dict()
        usuario =   form['usuario'] if form.get('usuario') else ''
        projeto =   form['projeto'] if form.get('projeto') else ''
        git =       form['git'] if form.get('git') else ''
        enderecos = form['enderecos'] if form.get('enderecos') else ''


    return render_template("tutorial.html",
                           usuario=usuario,
                           projeto=projeto,
                           git=git,
                           enderecos=re.sub(r'\s+', ' ', enderecos).strip().split(' '))

if __name__ == '__main__':
    app.run()