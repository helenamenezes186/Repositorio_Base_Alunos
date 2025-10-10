#1. Crie um programa que use um comando com o Pyautogui para abrir 
# a calculadora do Windows e faça um calculo de 8 + 2 e apresente o resultado.
#Observação: Utilizando o Win + R
#para abrir o Executar, digitar "calc"
#e pressionar Enter.

import pyautogui
import time

time.sleep(2)             # espera 2 segundos para você focar na tela
pyautogui.hotkey('win', 'r')  # abre o Executar
time.sleep(1)
pyautogui.write('calc')  # digita calc
pyautogui.press('enter')  # pressiona Enter
time.sleep(2)             # espera a calculadora abrir
pyautogui.write('8+2=')  # digita o cálculo
