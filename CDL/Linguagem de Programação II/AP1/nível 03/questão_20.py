# Gabriel Levi Lima Rodrigues
# Questão 20 – (1 ponto)
# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
# Até 5 Kg
# File Duplo      R$ 4,90 por Kg
# Alcatra         R$ 5,90 por Kg
# Picanha         R$ 6,90 por Kg
#
# Acima de 5 Kg
# File Duplo      R$ 5,80 por Kg
# Alcatra         R$ 6,80 por Kg
# Picanha         R$ 7,80 por Kg
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da
# promoção, porém não há limites para a quantidade de carne por cliente. Se compra for feita
# no  cartão  Tabajara  o  cliente  receberá  ainda  um  desconto  de  5%  sobre  o  total  da  compra.
# Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere
# um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total,
# tipo de pagamento, valor do desconto e valor a pagar.
from datetime import datetime

print(' ' * 5, '=*' * 5, 'Bem-Vindo', '=*' * 5)
print(' ' * 5, '=*' * 5, 'Hipermercado Tabajara', '=*' * 5)
cliente = input('Informe seu nome: ')

# Definição dos preços das carnes por Kg
precos = {
    'File Duplo': {'ate_5kg': 4.90, 'acima_5kg': 5.80},
    'Alcatra': {'ate_5kg': 5.90, 'acima_5kg': 6.80},
    'Picanha': {'ate_5kg': 6.90, 'acima_5kg': 7.80}
}

# Solitamos ao usuario que informe o tipo da carne e a quandidade requisitada.
while True:
    type_carne = input('Digite o tipo da carne (File Duplo, Alcatra, Picanha): ').strip().capitalize()
    if type_carne.lower() == "file duplo" or type_carne.lower() == "fileduplo":
        type_carne = "File Duplo"

    if type_carne in ['File Duplo', 'Alcatra', 'Picanha']:
        break
    else:
        print('Tipo de carne inválido. Por favor, digite "File Duplo", "Alcatra" ou "Picanha".')

print('*' * 5, 'ATENÇÃO!', '*' * 5,
      '\nObs: Caso o valor seja quebrado coloque (.), ex: 5.1, ou 2.3')
quant_carne = float(input('Informe a quantidade em Kg:'))

'''---------------------------------------------------------------------------------------------'''

# Teste de condições
# Verifica o preço de acordo com a quantidade comprada
if quant_carne <= 5:
    preco_total = quant_carne * precos[type_carne]['ate_5kg']
else:
    preco_total = quant_carne * precos[type_carne]['acima_5kg']
# Obs: o segundo colchete serve para acessar o dicionario dentro da chaves em 'precos'.

'''---------------------------------------------------------------------------------------------'''
# Perguntamos se a compra foi realizar pelo cartão da loja para que possa ser aplicado o desconto.
card_tabajara = input('A compra foi feita pelo cartão Tabajara? (S/N): ').upper()
if card_tabajara == 'S':
    desconto = preco_total * 0.05
    preco_total -= desconto
    type_paga = 'Cartão Tabajara'
else:
    desconto = 0
    type_paga = 'Outros'
'''---------------------------------------------------------------------------------------------'''

# Emissão de cupom
print(' ' * 5, '=*' * 5, 'Cupom Fiscal', '=*' * 5)
print('=*' * 5, 'Hipermercado Tabajara', '=*' * 5)
print('-' * 50)
print('Comprador: {}'.format(cliente))
print('Tipo de Carne: {}'.format(type_carne))
print('Quantidade: {:.2f}Kg'.format(quant_carne))
print('Preço Cheio: R${:.2f}'.format(preco_total))
print('Tipo do Pagamento: {}'.format(type_paga))
print('Valor do Desconto: R${:.2f}'.format(desconto))
print('Valor Total: R${:.2f}'.format(preco_total - desconto))

hoje = datetime.now()
print(f'Data de compra: {hoje:%d/%m/%y}, Hora: {hoje:%H:%M:%S}')
print('-' * 50)
print('=*' * 5, 'Obrigado e volte sempre!', '=*' * 5)
# Gabriel Levi Lima Rodrigues
