import random

import pyautogui as pg

import time

elogios = [
    "incrível",
    "fantástico",
    "talentoso",
    "inteligente",
    "formidável",
    "espetacular",
    "carismático",
    "amigável",
    "criativo",
    "dedicado",
    "eficiente",
    "elegante",
    "generoso",
    "habilidoso",
    "impressionante",
    "inovador",
    "inspirador",
    "magnífico",
    "notável",
    "produtivo",
    "sensacional",
    "versátil",
    "visionário"
]

time.sleep(8)

for i in range(200):
    a=random.choice(elogios)
    pg.write('vc e '+a)
    pg.press('enter')