# BD = "base.db"
# conexao = sqlite3.connect(BD) #nao precisa mais colocar uma em cada funçao
# cursor = conexao.cursor()


#
#
# Funções
#
# data = '2019-01-04'
# dia = [8:10]
# print(dia)
#
# mes = data[5:7]
# print(mes)
#
# ano = data[:4]
# print(ano)
#
# data_final= dia+'-'+mes+'-'+ano
# print(data_final)







data = '04-01-2019'
lista_data = data.split('-')
print(lista_data)

lista_data.reverse()
print(lista_data)

data_final = '-'.join(lista_data)
print(data_final)