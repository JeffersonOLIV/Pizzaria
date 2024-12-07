from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/')
def fazer_pedido():
    return render_template('fazer_pedido.html')

@app.route('/confirmar_pedido', methods=["POST"])
def confirmar_pedido():
    massa = request.form.get('')
    return render_template('confirmar_pedido.html', massa = massa)