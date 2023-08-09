def descricaoProduto(lista):
    resposta='S'
    while resposta == 'S':
        equipamento=[input('equipamento: '),
        float(input('valor: ')),
        int(input('numero de serie: ')),
        input('categoria: ')]
        lista.append(equipamento)
        resposta = input('digite \"s\" para continuar').upper()

def exibirProduto(lista):
  for elemento in lista:
      print('Nome..: ', elemento[0])
      print('Valor..: ', elemento[1])
      print('Serie..: ', elemento[2])
      print('Categoria..: ', elemento[3])

def localizarProduto(lista):
    busca=input('digite o nome do produto que deseja buscar: ')
    for elemento in lista:
        if busca==elemento[0]:
            print('Valor..: ', elemento[1])
            print('Serie..:', elemento[2])

def depreciarProduto(lista, porc):
    depreciar=input('Digite o nome do produto que deseja depreciar')
    for elemento in lista:
        if depreciar==elemento[0]:
            print('valor antigo do produto', elemento[1])
            elemento[1] = elemento[1] * (1-porc/100)
            print('Novo valor: ', elemento[1])

def excluirProdutoSerial(lista):
    serial=int(input('\Digite o serial do equipamento que será excluido: '))
    for elemento in lista:
        if elemento[2]==serial:
            lista.remove(elemento)
        return 'Item removido'
def resumirProduto(lista):
    valores=[]
    for elemento in lista:
        valores.append(elemento[1])
    if len(valores)>0:
        print('O equipamento mais caro custa: ', max(valores)),
        print('O equipamento mais barato custa: ', min(valores)),
        print('O total de equipamento é: ', sum(valores))




