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

        if "xxx" in pole:
            return redirect(url_for("vyhra"))

        if "ooo" in pole:
            return redirect(url_for("prohra"))

        if "-" not in pole:
            return redirect(url_for("remiza"))


        return redirect(url_for('piskvorky', pole=pole))


@app.route('/vyhra')
def vyhra():
    return render_template('vyhra.html')

@app.route('/prohra')
def prohra():
    return render_template('prohra.html')

@app.route('/remiza')
def remiza():
    return render_template('remiza.html')
