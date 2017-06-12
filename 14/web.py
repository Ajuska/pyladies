from flask import Flask, render_template, redirect, url_for
from tahnuti import tah
from ai import tah_pocitace, tah
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/druha_stranka')
def druha_stranka():
    return "Druhá stranka"

@app.route('/users/<name>')
def user(name):
    return render_template('uziv.html', name=name.upper())

@app.route('/piskvorky/<pole>')
@app.route('/piskvorky/<pole>/<pozice>')
def piskvorky(pole, pozice=None):
    if pozice == None:
        return render_template('piskvorky.html', pole=pole)
    else:
        pozice = int(pozice)
        pole = tah(pole, pozice, 'x') #naimportuje si tah


        if "xxx" not in pole:
            pole = tah_pocitace(pole, 'o')

        if "xxx" in pole or "ooo" in pole:
            return redirect(url_for("hello"))#presmerovat na gratuluji/vyhral pc

        return redirect(url_for('piskvorky', pole=pole))
