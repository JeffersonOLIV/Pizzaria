from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fazer_pedido', methods=['GET', 'POST'])
def fazer_pedido():
    if request.method == 'POST':
        massa = request.form.get('massa')
        borda = request.form.get('borda')
        molho = request.form.get('molho')
        queijo = request.form.get('queijo')
        return render_template('confirmar_pedido.html', massa=massa, borda=borda, molho=molho, queijo=queijo)
    
    return render_template('fazer_pedido.html')

@app.route('/confirmar_pedido', methods=["POST"])
def confirmar_pedido():
    massa = request.form.get('massa')
    return render_template('confirmar_pedido.html', massa=massa)

if __name__ == '__main__':
    app.run(debug=True)