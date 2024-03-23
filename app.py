from flask import Flask, jsonify, request

app = Flask(__name__)

surfistas = [
    {
        'id': 1,
        'nome': 'Gabriel Medina',
        'local': 'Brasil',
        'idade': 28
    },
    {
        'id': 2,
        'nome': 'John John Florence',
        'local': 'Hawaii',
        'idade': 29
    },
    {
        'id': 3,
        'nome': 'Italo Ferreira',
        'local': 'Brasil',
        'idade': 25
    },
]

# Consultar(todos)
@app.route('/surfistas', methods=['GET'])
def obter_surfistas():
    return jsonify(surfistas)

# Consultar por id
@app.route('/surfistas/<int:id>', methods=['GET'])
def obter_surfista_por_id(id):
    for surfista in surfistas:
        if surfista.get('id') == id:
            return jsonify(surfista)

# Editar
@app.route('/surfistas/<int:id>', methods=['PUT'])
def editar_surfista_por_id(id):
    surfista_alterado = request.get_json()
    for indice, surfista in enumerate(surfistas):
        if surfista.get('id') == id:
            surfistas[indice].update(surfista_alterado)
            return jsonify(surfistas[indice])

# Criar
@app.route('/surfistas', methods=['POST'])
def incluir_novo_surfista():
    novo_surfista = request.get_json()
    surfistas.append(novo_surfista)
    return jsonify(surfistas)

# Excluir
@app.route('/surfistas/<int:id>', methods=['DELETE'])
def excluir_surfista(id):
    for indice, surfista in enumerate(surfistas):
        if surfista.get('id') == id:
            del surfistas[indice]
    return jsonify(surfistas)

app.run(port=5000, host='localhost', debug=True)
