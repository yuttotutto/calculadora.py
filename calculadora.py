# calculadora.py versão 1.0
# Este programa foi desenvolvido por José Emanuel Sartor em 21/05/2021
# HavanProLabs
# Leia o arquivo README antes de executar 
# coding: UTF-8
from time import sleep
from datetime import date
import requests
import json
dia = date.today().day
mes = date.today().month
ano = date.today().year
get_cotacao = requests.get("https://api.hgbrasil.com/finance") #API da HG Brasil

COTACAO = json.loads(get_cotacao.text)

moedas = ('Real', 'Dólar', 'Euro', 'Libra')
sigla = ('R$', 'US$', '€', '£')
print('-=' *21)
print('Bem vindo a casa de câmbio Muito Dinheiro')
print('-=' *21)
print('Efetue o seu cadastro')
print('Insira o seu nome: ')
cliente = str(input(''))
print('Arquivando...')
sleep(1)
while True:
    print('Qual sua moeda de origem?')
    print('[ 0 ] Real')
    moedaorigem = int(input('Insira sua opção: '))
    if moedaorigem == 0:
        print('Sua moeda de origem é {}, Confirmar?' .format(moedas[moedaorigem]))
        print('[ 1 ] Confirmar')
        print('[ 2 ] Cancelar')
        option = int(input('Insira sua opção: '))
        if option == 1:
            break
        else:
            print('Opção Inválida')
            pass
print('=' *20)
print('=' *20)
while True:
    print('Qual sua moeda de destino?')
    print('[ 0 ] Real')
    print('[ 1 ] Dólar')
    print('[ 2 ] Euro')
    print('[ 3 ] Libra')
    destino = int(input('Insira sua opção: '))
    if moedaorigem == destino:
        print('A moeda de destino não pode ser igual a moeda de origem!')
        sleep(3)
        pass
    elif destino == 1 or destino == 2 or destino == 3:
        print('Sua moeda de destino é {}, Confirmar?' .format(moedas[destino]))
        print('[ 1 ] Confirmar')
        print('[ 2 ] Cancelar')
        option2 = int(input('Insira sua opção: '))
        if option2 == 1:
            break
        elif option2 == 2:
            pass
        else:
            print('Opção Inválida')
            pass
    else:
        print('Opção Inválida')
        pass

BRL = 0
USD = COTACAO["results"]["currencies"]["USD"]["buy"]
EUR = COTACAO["results"]["currencies"]["EUR"]["buy"]
GBP = COTACAO["results"]["currencies"]["GBP"]["buy"]
lista = [BRL, USD, EUR, GBP]
print('=' *47)
print('Seja bem vindo a casa de câmbio Muito Dinheiro!')
print('Como você deseja retirar o seu dinheiro?')
print('=' *47)
print('[ 1 ] Moeda em Espécie')
print('[ 2 ] Cartão de Viagem')
print('[ 3 ] Casa de Câmbio')
option3 = int(input('Insira sua opção: '))
if option3 == 1:
    print('=' *32)
    print('Comprar {} em espécie' .format(moedas[destino]))
    print('Cotação atual {}{:.2f} + IOF (1.1%)' .format(sigla[destino], lista[destino]))
    print('=' *32)
    taxa = '(1.1%)'
    valor = float(input('Insira o valor da compra R$'))
    calc = valor / lista[destino]
    iof = calc + calc * 1.1 / 100
    print('Sua compra no valor de {}{:.2f} está sendo processada... ' .format(sigla[destino], iof))
    sleep(2)
    print('Compra aprovada no valor de {}{:.2f} Data: {}/{}/{}' .format(sigla[destino], iof, dia, mes, ano))
elif option3 == 2:
    print('=' *32)
    print('Comprar {} no cartão de viagem' .format(moedas[destino]))
    print('Cotação atual {}{:.2f} + IOF (6.38%)' .format(sigla[destino], lista[destino]))
    print('=' *32)
    taxa = '(6.38%)'
    valor = float(input('Insira o valor da compra R$'))
    calc = valor / lista[destino]
    iof = calc + calc * 6.38 / 100
    print('Sua compra no valor de {}{:.2f} está sendo processada... ' .format(sigla[destino], iof))
    sleep(2)
    print('Compra aprovada no valor de {}{:.2f} Data: {}/{}/{}' .format(sigla[destino], iof, dia, mes, ano))
elif option3 == 3:
    print('=' *50)
    print('Comprar {} na casa de câmbio Muito Dinheiro' .format(moedas[destino]))
    print('Cotação atual {}{:.2f} + Taxas (10%)' .format(sigla[destino], lista[destino]))
    print('=' *50)
    taxa = '(10%)'
    valor = float(input('Insira o valor da compra R$'))
    calc = valor / lista[destino]
    iof = calc + calc * 10 / 100
    print('Sua compra no valor de {}{:.2f} está sendo processada... ' .format(sigla[destino], iof))
    sleep(2)
    print('☑' *47)
    print('Compra aprovada no valor de {}{:.2f} Data: {}/{}/{}' .format(sigla[destino], iof, dia, mes, ano))
    print('☑' *47)
else:
    print('Opção Inválida')
print('-=' *19)
print('Checar o histórico de transações')
print('[ 1 ] Sim')
print('[ 2 ] Não')
print('-=' *19)
option4 = int(input('Insira sua opção: '))
if option4 == 1:
    print('-=' *20)
    print('Ultima operação de câmbio')
    print('Nome do cliente: {}' .format(cliente))
    print('Data: {}/{}/{}' .format(dia, mes, ano))
    print('Moeda de Origem: {}' .format(moedas[moedaorigem]))
    print('Moeda de Destino: {}' .format(moedas[destino]))
    print('Você paga {}{:.2f}' .format(sigla[moedaorigem], valor))
    print('Você recebe {}{:.2f}' .format(sigla[destino], iof))
    print('Taxa cobrada: {}' .format(taxa))
    print('-=' *20)
elif option == 2:
    exit()
else:
    exit()
input()
