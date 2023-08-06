from flask import Flask, jsonify, request, redirect, url_for
import sqlite3


app = Flask(__name__)


@app.route("/")
def home():
    return "Hello World, from Flask"

# con = sqlite3.connect("produtos.db")
# cur=con.cursor()

# prod={"nome":"arroz", "preco":1.75, "categoria":"cereal", "fornecedor":"Continente", "data_validade":"2025-05-07"}

# # cur.execute("CREATE TABLE produto(id integer PRIMARY KEY, \
# #             Nome varchar(20) NOT NULL, Preco real NOT NULL, Categoria varchar(20) NOT NULL,\
# #             Fornecedor varchar(20) NOT NULL, Data_Validade varchar(20) NOT NULL)")

# values=[]
# for valor in prod.values():
#     values.append(valor)



# cur.execute("INSERT INTO produto (Nome, Preco, Categoria, Fornecedor, Data_Validade) VALUES (?,?,?,?,?)", values)
# con.commit()




### criar

@app.route('/produtos',methods=['POST'])
def incluir_novo_produto():
    
    novo_produto = request.get_json()

    values=[]
    for valor in novo_produto.values():
        values.append(valor)

    con = sqlite3.connect("produtos.db")
    cur=con.cursor()

    cur.execute("INSERT INTO produto (Nome, Preco, Categoria, Fornecedor, Data_Validade) VALUES (?,?,?,?,?)", values)
    con.commit()

    return redirect(url_for("obter_produtos"))


### Consultar todos

@app.route('/produtos', methods=['GET'])
def obter_produtos():

    produtos=[]
    con = sqlite3.connect("produtos.db")
    cur=con.cursor()
    for i in cur.execute("SELECT * FROM produto"):
        produtos.append({"id":i[0], "Nome":i[1], "Preco":i[2], "Categoria":i[3], "Fornecedor":i[4], "Data_Validade":i[5]})

    return jsonify(produtos)


### Consultar por id

@app.route('/produtos/<int:id>',methods=['GET'])
def obter_produto_por_id(id):

    produtos=[]
    con = sqlite3.connect("produtos.db")
    cur=con.cursor()
    for i in cur.execute("SELECT * FROM produto"):
        produtos.append({"id":i[0], "Nome":i[1], "Preco":i[2], "Categoria":i[3], "Fornecedor":i[4], "Data_Validade":i[5]})

    for produto in produtos:
        if produto.get('id') == id:
            return jsonify(produto)
        
        
### Editar por id

@app.route('/produtos/<int:id>',methods=['PUT'])
def editar_produto_por_id(id):

    produtos=[]
    con = sqlite3.connect("produtos.db")
    cur=con.cursor()
    for i in cur.execute("SELECT * FROM produto"):
        produtos.append({"id":i[0], "Nome":i[1], "Preco":i[2], "Categoria":i[3], "Fornecedor":i[4], "Data_Validade":i[5]})
    
    produto_alterado = request.get_json()
    for indice, produto in enumerate(produtos):
        if produto.get('id') == id:
            produtos[indice].update(produto_alterado)



            cur.execute(f"Update produto set Nome = '{produto.get('Nome')}', Preco = '{produto.get('Preco')}', Fornecedor = '{produto.get('Fornecedor')}', \
                         Data_Validade = '{produto.get('Data_Validade')}' where id = '{id}'")
            con.commit()
    return redirect(url_for("obter_produtos"))
        

### Apagar por id

@app.route('/produtos/<int:id>',methods=['DELETE'])
def excluir_jogador(id):
    con = sqlite3.connect("produtos.db")
    cur=con.cursor()

    cur.execute("DELETE from produto where id = ?", (id,))
    con.commit()

    return redirect(url_for("obter_produtos"))
            


app.run(port=5000,host='localhost',debug=True)