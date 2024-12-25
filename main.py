import pyautogui as pg
import random
import time

# time.sleep(3)

# for i in range(278):
#     pg.write(f'lista.push(obj[{i}].innerText);')
#     pg.press('enter')
#     time.sleep(0.5)

personas = []

archivo = open("C:\\Codigos\\bot-comentarios\\lista_ig.txt")
num = 3

nlinea = 1

for linea in archivo:
    word = linea.split()
    if(len(word)) == 0: continue
    if nlinea == num:
        donde = word[0].find('\"')
        new = word[0]
        palabra = new[donde + 1:]
        palabra = palabra[:len(palabra) - 1]
        personas.append(palabra)
        print(palabra)
        num = num + 3
    nlinea += 1

time.sleep(5)

for i in range(278):
    a = random.choice(personas)

    pg.hotkey('ctrl', 'alt', 'q')
    pg.write(a)
    time.sleep(1)
    pg.click(x=1377, y=695)

    time.sleep(60)