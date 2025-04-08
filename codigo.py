import pyautogui
from time import sleep

# pyautogui -> fazer automações com python
#pyautogui.click - clicar em algo
#pyautogui.press - apertar 1 tecla
#pyautogui.write - escrever um texto
#pyautogui.hotkey - combinação de teclas

pyautogui.PAUSE = 0.5

# PASSO 1: Entrar no sistema da empresa : https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.press('win')
pyautogui.write('Microsoft Edge')
pyautogui.press('enter')

pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
sleep(3)

# PASSO 2 : Fazer login
pyautogui.click(x=389, y=358)
pyautogui.write('emailtest@hotmail.com')
pyautogui.press('tab')
pyautogui.write('senhatest')
pyautogui.press('tab')
pyautogui.press('enter')
sleep(3)

# PASSO 3 : Importrar a base de dados
import pandas
tabela = pandas.read_csv('produtos.csv')
print(tabela)

# PASSO 4 : Cadastrar um produto e Repetir para todos os outros produtos
for linha in tabela.index:
    pyautogui.click(x=415, y=251)

    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write(codigo)
    pyautogui.press('tab')

    marca = tabela.loc[linha, 'marca']
    pyautogui.write(marca)
    pyautogui.press('tab')

    tipo = tabela.loc[linha, 'tipo']
    pyautogui.write(tipo)
    pyautogui.press('tab')

    categoria = str(tabela.loc[linha, 'categoria'])
    pyautogui.write(categoria)
    pyautogui.press('tab')

    preco_unitario = str(tabela.loc[linha, 'preco_unitario'])
    pyautogui.write(preco_unitario)
    pyautogui.press('tab')

    custo = str(tabela.loc[linha, 'custo'])
    pyautogui.write(custo)
    pyautogui.press('tab')

    obs = str(tabela.loc[linha, 'obs'])
    if obs != 'nan':
        pyautogui.write(obs)

    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.scroll(10000)#voltar para o inicio da pagina






