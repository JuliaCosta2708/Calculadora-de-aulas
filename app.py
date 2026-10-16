
from flask import Flask, render_template, request

app = Flask(__name__)

horaAula = 55.00


def calcular_valor_aula(duracao: int) -> float:
    return horaAula * duracao / 60


def calcular_subtotal(quantidade: int, duracao: int) -> float:
    return quantidade * calcular_valor_aula(duracao)


@app.route("/", methods=["GET", "POST"])
def inicio():
    subtotal60 = 0
    subtotal45 = 0
    subtotal30 = 0
    total_geral = 0

    quantidade60 = 0
    quantidade45 = 0
    quantidade30 = 0

    if request.method == "POST":
        quantidade60 = int(request.form["quantidade60"])
        quantidade45 = int(request.form["quantidade45"])
        quantidade30 = int(request.form["quantidade30"])

        subtotal60 = calcular_subtotal(quantidade60, 60)
        subtotal45 = calcular_subtotal(quantidade45, 45)
        subtotal30 = calcular_subtotal(quantidade30, 30)

        total_geral = subtotal60 + subtotal45 + subtotal30

    return render_template(
        "index.html",
        horaAula=horaAula,
        quantidade60=quantidade60,
        quantidade45=quantidade45,
        quantidade30=quantidade30,
        subtotal60=subtotal60,
        subtotal45=subtotal45,
        subtotal30=subtotal30,
        total_geral=total_geral
    )


if __name__ == "__main__":
    app.run(debug=True)
