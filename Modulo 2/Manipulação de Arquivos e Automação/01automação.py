# 1º Passo: Instalar o Pyautogui com o comando:
# pip install pyautogui

# Crie uma automação que abra automaticamente um navegador

# Importamos a biblioteca para o script em uso
import pyautogui

# 'press' é um comando que utilizamos para pressionar a tecla desejada
pyautogui.press ('Win') # para pressionar a tecla windows

# 'sleep' é um comando que utilizamos nara deixar o código
# em espera por a (seconds: float) -> None
pyautogui. sleep(1)

# 'Write' é um comando que utilizamos para passar o que queremos
# escrever
pyautogui.write('Google Crhome')

pyautogui.press('enter')