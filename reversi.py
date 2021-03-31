'''
Author: Maciej Kaczkowski
26.03-xx.04.2021
'''


import pygame as pg


pg.init()
win = pg.display.set_mode((500, 500))
pg.display.set_caption("Reversi")
run = True

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
