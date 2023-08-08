from flask import Flask, jsonify, request, redirect, url_for, render_template
from flask_cors import CORS
import sqlite3
import base64
from PIL import Image
from io import BytesIO


app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return render_template('index.html')



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

### criar

@app.route('/produts',methods=['POST','GET'])
def incluir_novo_produto():
    
    # novo_produto = request.get_json()

    # values=[]
    # for valor in novo_produto.values():
    #     values.append(valor)

    if request.method=='POST':

        nome = request.form["nome"]
        preco = request.form["preco"]
        categoria = request.form["categoria"]
        fornecedor = request.form["fornecedor"]
        data_validade = request.form["dataval"]
        # imag = request.form["img"]

        # with open("imag.jpg", "rb") as image_file:
        #     data = base64.b64encode(image_file.read())
    

    # con = sqlite3.connect("produts.db")
    # cur=con.cursor()

    # cur.execute("INSERT INTO produt (Nome, Preco, Categoria, Fornecedor, Data_Validade, Imagem) VALUES (?,?,?,?,?,?)",(nome, preco, categoria, fornecedor,data_validade, data))
    # con.commit()

    return redirect(url_for("obter_produtos"))


### Consultar todos

@app.route('/produts', methods=['GET'])
def obter_produtos():

    produts=[]
    con = sqlite3.connect("produts.db")
    cur=con.cursor()
    for i in cur.execute("SELECT * FROM produt"):
        produts.append({"id":i[0], "Nome":i[1], "Preco":i[2], "Categoria":i[3], "Fornecedor":i[4], "Data_Validade":i[5]})

    return jsonify(produts)


# ### Consultar por id

# @app.route('/produtos/<int:id>',methods=['GET'])
# def obter_produto_por_id(id):

#     produtos=[]
#     con = sqlite3.connect("produtos.db")
#     cur=con.cursor()
#     for i in cur.execute("SELECT * FROM produto"):
#         produtos.append({"id":i[0], "Nome":i[1], "Preco":i[2], "Categoria":i[3], "Fornecedor":i[4], "Data_Validade":i[5]})

#     for produto in produtos:
#         if produto.get('id') == id:
#             return jsonify(produto)
        
        
# ### Editar por id

# @app.route('/produtos/<int:id>',methods=['PUT'])
# def editar_produto_por_id(id):

#     produtos=[]
#     con = sqlite3.connect("produtos.db")
#     cur=con.cursor()
#     for i in cur.execute("SELECT * FROM produto"):
#         produtos.append({"id":i[0], "Nome":i[1], "Preco":i[2], "Categoria":i[3], "Fornecedor":i[4], "Data_Validade":i[5]})
    
#     produto_alterado = request.get_json()
#     for indice, produto in enumerate(produtos):
#         if produto.get('id') == id:
#             produtos[indice].update(produto_alterado)



#             cur.execute(f"Update produto set Nome = '{produto.get('Nome')}', Preco = '{produto.get('Preco')}', Fornecedor = '{produto.get('Fornecedor')}', \
#                          Data_Validade = '{produto.get('Data_Validade')}' where id = '{id}'")
#             con.commit()
#     return redirect(url_for("obter_produtos"))
        

# ### Apagar por id

# @app.route('/produtos/<int:id>',methods=['DELETE'])
# def excluir_jogador(id):
#     con = sqlite3.connect("produtos.db")
#     cur=con.cursor()

#     cur.execute("DELETE from produto where id = ?", (id,))
#     con.commit()

#     return redirect(url_for("obter_produtos"))
            




if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')