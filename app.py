from flask import Flask, jsonify
import math

app = Flask(__name__)

@app.route("/calc/<int:n>", methods=["GET"])
def calc(n: int):
    # Validaciones
    if n < 0:
        return jsonify({"error": "El factorial solo está definido para enteros no negativos.", "numero": n}), 400
    if n > 2000:
        # límite para evitar tiempos y memoria excesivos
        return jsonify({"error": "Número demasiado grande para calcular factorial de forma segura.", "numero": n}), 413

    try:
        fact = math.factorial(n)
    except (OverflowError, ValueError) as e:
        return jsonify({"error": "No fue posible calcular el factorial.", "detalle": str(e)}), 500

    etiqueta = "par" if (n % 2 == 0) else "impar"
    return jsonify({"Número": n, "Factorial": fact, "Etiqueta": etiqueta})

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"Estado": "ok"}), 200

if __name__ == "__main__":
    # Para desarrollo local
    app.run(host="0.0.0.0", port=8000, debug=True)
