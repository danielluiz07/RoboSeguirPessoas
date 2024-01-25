import pyautogui
import time

#Da um tempo de 10s para o programa funcionar
time.sleep(10)

#Variável que dirá o tempo que o programa rodará (em segundos)
tempoMaximo = 1200

#Cria a variável do tempo inicial 
tempoInicial = time.time()

while (time.time() - tempoInicial) < tempoMaximo:
    #entra na página do insta
    pyautogui.click(x=788, y=584)
    time.sleep(7)


    #Segue as pessoas
    pyautogui.click(x=730, y=133)
    time.sleep(2)
    pyautogui.click(x=790, y=133)
    time.sleep(2)
    pyautogui.click(x=850, y=133)
    time.sleep(4)

    #elimina a página do instagram
    pyautogui.hotkey('ctrl', 'w')
    time.sleep(3)

    #Clica em confirmar ação 
    pyautogui.click(x=740, y=575)
    
    #espera 2segundps para começar o loop novamente
    time.sleep(2)
