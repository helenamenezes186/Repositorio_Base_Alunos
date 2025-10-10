# Efeito "matrix" no Bloco de Notas
# após executar o código abra um bloco de notas novo

import pyautogui, time, random

time. sleep(3)
chars = "01"
for i in range(200):
    pyautogui.write(random.choice(chars), interval=0.02)