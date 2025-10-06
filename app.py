from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/soma', methods=['GET'])
def soma():
        valor1 = float(request.args.get("valor1"))
        valor2 = float(request.args.get("valor2"))
        resultado = valor1 + valor2
    return jsonify ({"mensagem", "resultado encontrado": resultado}),200
    return jsonify ({"mensagem", "resultado nao encontardo": resultado})404

@app.route('/subtrair', methods=['GET'])
def subtrair():
        valor1 = float(request.args.get("valor1"))
        valor2 = float(request.args.get("valor2"))
        resultado = valor1 - valor2
   return jsonify ({"mensagem", "resultado": resultado}),200
   return jsonify ({"mensagem", "resultado nao encontrado": resultado})404

@app.route('/multiplicar', methods=['GET'])
def multiplicar():
        valor1 = float(request.args.get("valor1"))
        valor2 = float(request.args.get("valor2"))
        resultado = valor1 * valor2
    return jsonify ({"mensagem", "resultado": resultado}),200
    return jsonify ({"mensagem", "resultado nao encontardo": resultado})404

@app.route('/dividir', methods=['GET'])
def dividir():
        valor1 = float(request.args.get("valor1"))
        valor2 = float(request.args.get("valor2"))
        resultado = valor1 / valor2
        if valor2 == 0:
           return {"erro": "divisao por zero nao e permitida"}
    return jsonify ({"mensagem", "resultado": resultado}),200

if __name__ == '__main__':
    app.run(debug=True)