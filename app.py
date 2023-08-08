from flask import Flask, jsonify, request, redirect, url_for, render_template
from flask_cors import CORS
import sqlite3
import base64
from PIL import Image
from io import BytesIO


app = Flask(__name__)
CORS(app)


@app.route("/",methods=['GET'])
def home():


    return "Bem Vindo à página"  #render_template('index.html')



con = sqlite3.connect("Produtos.db")
cur=con.cursor()

def com():

    # prod={"nome":"arroz", "preco":1.75, "categoria":"cereal", "fornecedor":"Continente", "data_validade":"2025-05-07"}

    # cur.execute("CREATE TABLE produto(idProduto integer PRIMARY KEY AUTOINCREMENT, codigoProduto varchar(20),\
    #             nomeProduto varchar(20) NOT NULL, descricaoProduto varchar(20) NOT NULL, corProduto varchar(20) NOT NULL, \
    #             quantidadeProduto integer, dataValidadeProduto varchar(20), marcaProduto varchar(20), precoUnitarioProduto real NOT NULL, \
    #             categoriaProduto varchar(20) NOT NULL, fornecedorProduto varchar(20) NOT NULL, imagemProduto)")

    # values=[]
    # for valor in prod.values():
    #     values.append(valor)



    # cur.execute("INSERT INTO produto (Nome, Preco, Categoria, Fornecedor, Data_Validade) VALUES (?,?,?,?,?)", values)
    # con.commit()



    # @app.route('/img',methods=['GET','POST'])
    # def img():

    #     if request.method=='POST':

    #         imag = request.form["img"]

    #         with open("imag", "rb") as image_file:
    #             data = base64.b64encode(image_file.read())

    #     val='abcdef'

    #     return redirect(url_for("obter_produtos"))
        

    # im = Image.open(BytesIO(base64.b64decode(data)))
    # im.save('image1.png', 'PNG')

    return "nada"



## criar

@app.route('/produtos',methods=['POST'])
def incluir_novo_produto():
    
    novo_produto = request.get_json()

    values=[]
    for valor in novo_produto.values():
        values.append(valor)

        # imag = request.form["img"]

        # with open("imag.jpg", "rb") as image_file:
        #     data = base64.b64encode(image_file.read())
    

    con = sqlite3.connect("produtos.db")
    cur=con.cursor()

    cur.execute("INSERT INTO produto (codigoProduto, nomeProduto, descricaoProduto, corProduto, quantidadeProduto, \
                dataValidadeProduto, marcaProduto, precoUnitarioProduto, categoriaProduto, fornecedorProduto, imagemProduto) \
                VALUES (?,?,?,?,?,?,?,?,?,?,?)", values)
    con.commit()

    return redirect(url_for("obter_produtos"))


### Consultar todos

@app.route('/produtos', methods=['GET'])
def obter_produtos():

    produtos=[]
    con = sqlite3.connect("produtos.db")
    cur=con.cursor()
    for i in cur.execute("SELECT * FROM produto"):
        produtos.append({"idProduto":i[0], "codigoProduto":i[1], "nomeProduto":i[2], "descricaoProduto":i[3], 
                         "corProduto":i[4], "quantidadeProduto":i[5], "dataValidadeProduto":i[6], 
                         "marcaProduto":i[7], "precoUnitarioProduto":i[8], "categoriaProduto":i[9], 
                         "fornecedorProduto":i[10], "imagemProduto":i[11]})

    return jsonify(produtos)


### Consultar por id

@app.route('/produtos/<int:id>',methods=['GET'])
def obter_produto_por_id(id):

    produtos=[]
    con = sqlite3.connect("produtos.db")
    cur=con.cursor()
    for i in cur.execute("SELECT * FROM produto"):
        produtos.append({"idProduto":i[0], "codigoProduto":i[1], "nomeProduto":i[2], "descricaoProduto":i[3], 
                         "corProduto":i[4], "quantidadeProduto":i[5], "dataValidadeProduto":i[6], 
                         "marcaProduto":i[7], "precoUnitarioProduto":i[8], "categoriaProduto":i[9], 
                         "fornecedorProduto":i[10], "imagemProduto":i[11]})

    for produto in produtos:
        if produto.get('idProduto') == id:
            return jsonify(produto)
        
        
### Editar por id

@app.route('/produtos/<int:id>',methods=['PUT'])
def editar_produto_por_id(id):

    produtos=[]
    con = sqlite3.connect("produtos.db")
    cur=con.cursor()
    for i in cur.execute("SELECT * FROM produto"):
        produtos.append({"idProduto":i[0], "codigoProduto":i[1], "nomeProduto":i[2], "descricaoProduto":i[3], 
                         "corProduto":i[4], "quantidadeProduto":i[5], "dataValidadeProduto":i[6], 
                         "marcaProduto":i[7], "precoUnitarioProduto":i[8], "categoriaProduto":i[9], 
                         "fornecedorProduto":i[10], "imagemProduto":i[11]})
    
    produto_alterado = request.get_json()
    for indice, produto in enumerate(produtos):
        if produto.get('idProduto') == id:
            produtos[indice].update(produto_alterado)



            cur.execute(f"Update produto set codigoProduto = '{produto.get('codigoProduto')}', nomeProduto = '{produto.get('nomeProduto')}', descricaoProduto = '{produto.get('descricaoProduto')}', \
                         corProduto = '{produto.get('corProduto')}', quantidadeProduto = '{produto.get('quantidadeProduto')}', dataValidadeProduto = '{produto.get('dataValidadeProduto')}', \
                         marcaProduto = '{produto.get('marcaProduto')}', precoUnitarioProduto = '{produto.get('precoUnitarioProduto')}', categoriaProduto = '{produto.get('categoriaProduto')}', \
                         fornecedorProduto = '{produto.get('fornecedorProduto')}', imagemProduto = '{produto.get('imagemProduto')}' where idProduto = '{id}'")
            con.commit()
    return redirect(url_for("obter_produtos"))
        

### Apagar por id

@app.route('/produtos/<int:id>',methods=['DELETE'])
def excluir_produto(id):
    con = sqlite3.connect("produtos.db")
    cur=con.cursor()

    cur.execute("DELETE from produto where idProduto = ?", (id,))
    con.commit()

    return redirect(url_for("obter_produtos"))
            

## Consultar por categoria

@app.route('/produtos/<categoria>',methods=['GET'])


def obter_produto_por_categoria(categoria):

    produtos=[]
    lista_produtos_categoria=[]
    con = sqlite3.connect("produtos.db")
    cur=con.cursor()
    for i in cur.execute("SELECT * FROM produto"):
        produtos.append({"idProduto":i[0], "codigoProduto":i[1], "nomeProduto":i[2], "descricaoProduto":i[3], 
                         "corProduto":i[4], "quantidadeProduto":i[5], "dataValidadeProduto":i[6], 
                         "marcaProduto":i[7], "precoUnitarioProduto":i[8], "categoriaProduto":i[9], 
                         "fornecedorProduto":i[10], "imagemProduto":i[11]})

    for produto in produtos:
        if produto.get('categoriaProduto') == categoria.lower():
            lista_produtos_categoria.append(produto)
        
    return jsonify(lista_produtos_categoria)



if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')