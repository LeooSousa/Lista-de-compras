import sqlite3

BD = "base.db"


def add_compra(Data):
    '''Adciona uma compra'''
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = " INSERT INTO Compras ( Data, Total) VALUES ( '%s', '%d' )" % (Data, 0)
    cursor.execute(sql)
    if cursor.rowcount == 1:
        conexao.commit()
        print("Lista", Data, "Criada")
    else:
        conexao.rollback()
        print("Nao foi possivel  criar a lista")
        cursor.close()
        conexao.close()


def get_total(Id_compra):
    '''Calcula o total da compra'''
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = " SELECT Total FROM Compras WHERE Id_compra= '%d'" % Id_compra
    cursor.execute(sql)
    total = cursor.fetchone()
    if total:
        return total[0]


##########################################################
def exibir_listas():
    '''Exibi as listas'''
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = " SELECT * FROM Compras"
    cursor.execute(sql)
    compras = cursor.fetchall()
    if compras:
        for compra in compras:
            print("Id compra: ", compra[0], " - Data da compra: ", compra[1], " - Total da compra: ", compra[2])
    else:
        print("Nao foi possivel  criar a lista")
        cursor.close()
        conexao.close()


####################################################
def listar_produtos(Id_compra):
    conexao = sqlite3.connect(BD)  # sempre preciso criar conexao com o banco
    sql = "SELECT * FROM Produto where Id_compra == '%s'" % Id_compra
    cursor = conexao.cursor()  # pego os codigos roda no bd
    cursor.execute(sql)
    Produtos = cursor.fetchall()  # seleciona tudo ta tabela
    if Produtos.__len__() > 0:
        for Produto in Produtos:
            print("Id_produto: ", Produto[0], ' - Descrição:', Produto[1], " - Quantidade: ", Produto[2],
                  " - Valor_unitario: ", Produto[3])
    else:
        print("Nenhum produto cadastrado!")
    cursor.close()
    conexao.close()

######################################################################################
def atualiza_total(Id_compra, Valor):
    total = get_total(Id_compra) + Valor
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = "UPDATE Compras SET Total= '%d' WHERE Id_compra = '%d'" %(total, Id_compra)
    cursor.execute(sql)
    if cursor.rowcount == 1:
        conexao.commit()
        return True
    else:
        conexao.rollback()
    cursor.close()
    conexao.close()




######################################################################

def inserir_produto_lista(Descricao, Quantidade, Valor_unitario, Id_compra):
    '''ojhiugh'''
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = ("INSERT INTO Produto (Descricao, Quantidade, Valor_unitario, Id_compra) VALUES ('%s', '%d', '%s', '%d')"
           % (Descricao, Quantidade, Valor_unitario, Id_compra))
    cursor.execute(sql)
    if cursor.rowcount == 1:
        conexao.commit()
        atualiza_total(Id_compra, Valor_unitario * Quantidade)
        print("Produto", Descricao, "cadastrado")
    else:
        conexao.rollback()
        print("Nao foi possivel cadastrar o produto")
    cursor.close()
    conexao.close()


##########################################################################

def buscar_por_id(Id_produto,Id_compra):
    conexao = sqlite3.connect(BD)  # sempre preciso criar conexao com o banco
    cursor = conexao.cursor()  # pego os codigos roda no bd
    sql = "SELECT * FROM Produto WHERE Id_produto='%d' and Id_compra == '%s'" % (Id_produto, Id_compra)
    cursor.execute(sql)
    Produto = cursor.fetchone()
    if Produto:
        print("Id_produto: ", Produto[0], ' - Descrição:', Produto[1], " - Quantidade: ", Produto[2],
              " - Valor_unitario: ", Produto[3])
        return True
    else:
        print("Nenhum produto cadastrado!")

    cursor.close()
    conexao.close()


#########################################################################

def excluir_produto_p_id(Id_produto, Id_compra):
    if buscar_por_id(Id_produto, Id_compra):
        resposta = input("Deseja realmente excluir esse produto?").lower()
        if resposta == 's':
            conexao = sqlite3.connect(BD)
            cursor = conexao.cursor()
            sql = "DELETE FROM Produto WHERE Id_produto='%d' and Id_compra == '%s'" % (Id_produto, Id_compra)
            cursor.execute(sql)
            if cursor.rowcount == 1:
                conexao.commit()
                print('Produto deletado!')
            else:
                conexao.rollback()
                print("Nao foi possivel deletar produto")


#########################################################################
def alterar_preco(Id_produto, Id_compra):
    if buscar_por_id(Id_produto, Id_compra):
        Valor_unitario = float(input('Informe o novo preço do produto'))
        conexao = sqlite3.connect(BD)
        cursor = conexao.cursor()
        sql = "UPDATE Produto SET Valor_unitario='%d' WHERE Id_produto='%d' and Id_compra == '%s'" % (Valor_unitario, Id_produto, Id_compra)
        cursor.execute(sql)
        if cursor.rowcount == 1:
            conexao.commit()
            print('Produto alterado!')
        else:
            conexao.rollback()
            print('Não foi possível alterar produto')


##########################################################################
def alterar_descricao(Id_produto):
    if buscar_por_id(Id_produto):
        descricao = input('Informe a nova descrição do produto')
        conexao = sqlite3.connect(BD)
        cursor = conexao.cursor()
        sql = "UPDATE Produto SET Descricao='%s' WHERE Id_produto= '%d' " % (
            descricao, Id_produto)
        cursor.execute(sql)
        if cursor.rowcount == 1:
            conexao.commit()
            print('Produto alterado!')
        else:
            conexao.rollback()
            print('Não foi possível alterar produto')


##########################################################################

def buscar_por_descricao(Descricao):
    Descricao = Descricao + '%'
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = "SELECT * FROM produto WHERE Descricao LIKE '%s'" % Descricao
    cursor.execute(sql)
    Produtos = cursor.fetchall()
    if Produtos:
        for Produtos in Produtos:
            print("Id_produto: ", Produtos[0], ' - Descrição:', Produtos[1], " - Quantidade: ", Produtos[2],
                  " - Valor_unitario: ", Produtos[3])
        return True
    else:
        print("Nenhum produto encontrado!")
        return False

    cursor.close()
    conexao.close()


def somar_produtos(listar_produtos):
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()


print("#" * 40)
print("            MENU              ")
print(" 1 - Adicionar Compras")
print(" 2 - Cadastrar Produto")
print(" 3 - Listar todos os Produtos de uma determinada compra")
print(" 4 - Buscar Produto por ID")
print(" 5 - Excluir Produto por ID")
print(" 6 - Alterar preço")
print(" 7 - Alterar descrição")
print(" 8 - Buscar por descrição")
print(" 9 - Exibir listas de compra")
print(" 10 - Ver o total de determinada compra")
print(" 11 - Sair")
print("#" * 40)


op = 0
while op != 11:
    op = int(input("digite uma opção: "))
    if op == 1:
        Data = str(input("comece uma compra informando a data"))
        add_compra(Data)

    if op == 2:
        Descricao = input("Informe o nome do produto:")
        Quantidade = int(input("Informe a quantidade de produtos que irá comprar: "))
        Valor_unitario = int(input("Informe o valor do produto: "))
        Id_compra = int(input("Informe o código da compra: "))

        inserir_produto_lista(Descricao, Quantidade, Valor_unitario, Id_compra)

    if op == 3:
        Id_compra = input("Digite aqui o Id da compra que voce deseja listar:")
        listar_produtos(Id_compra)

    if op == 4:
        Id_compra = int(input("Informe o Id do compra: "))
        Id_produto = int(input("Informe o Id do produto: "))
        buscar_por_id(Id_produto,Id_compra)

    if op == 5:
        Id_compra = int(input("Informe o Id do compra: "))
        Id_produto = int(input("Informe o Id do produto: "))
        excluir_produto_p_id(Id_produto, Id_compra)

    if op == 6:
        Id_compra = int(input("Informe o Id do compra: "))
        Id_produto = int(input("Informe o Id do produto: "))
        alterar_preco = input("Informe o novo preço: ")
        alterar_preco(Id_produto, Id_compra)

    if op == 7:
        descricao = input('Informe a nova descrição do produto')
        alterar_descricao(Id_produto)

    if op == 8:
        Descricao = input("Informe a descrição do produto: ")
        buscar_por_descricao(Descricao)

    if op == 9:
        exibir_listas()
        print(get_total(1))

    if op == 10:
        Id_compra = int(input("informe o ID da compra para ver o total: "))
        print(get_total(Id_compra))





# fazer a funçao para consultar a compra e depois dar o total de todos os produtos que o cliente quer comprar

# add_compra("2018-05-26")and Id_compra
# cadastrar("Notebook", 567, "10.22", 1)
# buscar_por_id(10)
# buscar_por_descricao('N')
# listar_produtos()
# excluir_produto_p_id(1)
# alterar_preco(10)
# alterar_descricao(10)
# exibir_listas()

ajeitar a parte de alterar preço e inserir as outras