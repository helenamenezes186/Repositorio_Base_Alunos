# importamos a biblioteca pyautogui
import pyautogui
#crie uma automação que faça o mouse se mover na forma de um quadro

for i in range(10):
    # a função .moveTo é uma função para movimento de mouse
# pyatutogui.moveTo(x,y, duration=em segundos)
    pyautogui.moveTo(100 + 10 * i, 100 + 10 * i, duration=0.25)
    pyautogui .moveTo(200 + 10 * i, 100 + 10 * i, duration=0.25)
    pyautogui.moveTo(200 + 10 * i, 200 + 10 * i, duration=0.25)
    pyautogui.moveTo(100 + 10 * i, 200 + 10 * i, duration=0.25)