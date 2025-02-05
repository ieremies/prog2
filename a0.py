import marimo

__generated_with = "0.10.12"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(
        r"""
        # Relembrar é viver!

        Para retomarmos as atividades, iremos começar com alguns exercícios:

        Acesse [OBI 2023, nível 1, fase 1](https://olimpiada.ic.unicamp.br/static/extras/obi2023/provas/ProvaOBI2023_f1p1.pdf).
        """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Questão 1, VAR""")
    return


@app.cell
def _():
    def var(x, y): ...
    return (var,)


@app.cell
def _(var):
    var(6, -2)  # tem que retornar 'N'
    return


@app.cell
def _(var):
    var(8, 2)  # tem que retornar 'S'
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ## Questão 2, Estoque

        Essa questão irá tocar no tópico de matrizes. 
        É algo que vocês verão em matemática no segundo ano, mas, por enquanto, pensem nelas como "tabelas".
        Cada linha e cada coluna são identificados por números (começando do zero).
        """
    )
    return


@app.cell
def _():
    def estoque(est, pedidos):
        """
        :est: é tabela de quantidade de cada tipo de cada tamanho. est[0][0] é a quantidade de peças do tipo 1 e tamanho 1, enquanto est[1][2] é a quantidade de peças do tipo 2 tamamho 3.
        :pedidos: é uma lista de pares (tipo, tamanho) representando cada pedido.
        """
        ...
    return (estoque,)


@app.cell
def _(estoque):
    estoque([[5, 2, 2], [6, 4, 0], [2, 1, 4], [1, 3, 2]], [[1, 1], [2, 3]])
    # Resultado deve ser 1
    return


@app.cell
def _(estoque):
    estoque([[1, 3, 2, 5]], [[1, 1], [2, 3]])
    # Resultado deve ser 3
    return


@app.cell
def _(mo):
    mo.md("""## Questão 3, Subsequência""")
    return


@app.cell
def _():
    def subsequencia(a, b): ...
    return (subsequencia,)


@app.cell
def _(subsequencia):
    subsequencia([1, 2, 3, 4, 5], [2, 3, 5])  # Resultado deve ser S
    return


@app.cell
def _(subsequencia):
    subsequencia([8, 17, 8, 21, 23], [8, 8, 21, 22])  # Resultado deve ser N
    return


if __name__ == "__main__":
    app.run()
