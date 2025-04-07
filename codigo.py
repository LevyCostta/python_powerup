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

# PASSO 4 : Cadastrar um produto
# PASSO 5 : Repetir para todos os produtos






