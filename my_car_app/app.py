from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Lista de carros para demonstração
carros = [
    {"id": 1, "marca": "Toyota", "modelo": "Corolla", "preco": 85000},
    {"id": 2, "marca": "Honda", "modelo": "Civic", "preco": 95000},
    {"id": 3, "marca": "Volkswagen", "modelo": "Polo", "preco": 75000},
]

@app.route('/')
def inicio():
    return render_template('car_sales.html')

@app.route('/carros', methods=['GET'])
def listar_carros():
    return jsonify(carros)

@app.route('/carros/<int:carro_id>', methods=['GET'])
def obter_carro(carro_id):
    carro = next((c for c in carros if c["id"] == carro_id), None)
    if carro:
        return jsonify(carro)
    return jsonify({"erro": "Carro não encontrado"}), 404

@app.route('/carros', methods=['POST'])
def criar_carro():
    dados = request.get_json()
    novo_carro = {
        "id": max([c["id"] for c in carros]) + 1 if carros else 1,
        "marca": dados.get("marca"),
        "modelo": dados.get("modelo"),
        "preco": dados.get("preco")
    }
    carros.append(novo_carro)
    return jsonify(novo_carro), 201

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
