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
    pg.hotkey('altright' , '2')
    pg.write(a)
    pg.press('enter')

    tiempo_aleatorio = random.randint(5, 30)
    print(f"Pausando por {tiempo_aleatorio} segundos...")
    time.sleep(tiempo_aleatorio)  # Pausa