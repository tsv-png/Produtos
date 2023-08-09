from Produto import *

minhaLista=[]
print('preenchendo')
descricaoProduto(minhaLista)
print('Exibindo')
exibirProduto(minhaLista)

print('Pesquisando')
localizarProduto(minhaLista)
depreciarProduto(minhaLista, 20)

print('Excluido')
print(excluirProdutoSerial(minhaLista))
exibirProduto(minhaLista)

print('Resumindo')
resumirProduto(minhaLista)