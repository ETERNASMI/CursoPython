from random import randint
import time
import pygame
pcn = randint(0, 5)
print('-==-' * 39)
print('Tente adivinhar em qual número estou a pensar entre 0 e 5 ...')
print('-==-' * 39)
n = int(input('Em qual número estou pensando?\n'))
print('PROCESSANDO...')
time.sleep(2)
if n == pcn:
    print('UAUU!!! VOCÊ VENCEU!! O numero em que pensei é {}!'.format(pcn))
    print('-==-' * 39)
    print('Então escute a musica que temos para você!!')
    pygame.mixer.init()
    pygame.mixer.music.load('66.mp3')
    pygame.mixer.music.play()
    time.sleep(360)
else:
    print('OPS!! QUANTA FALTA DE SORTE!! VOCÊ PERDEU!! O NÚMERO EM QUE PENSEI É O {} e não no {}!'.format(pcn, n))
    time.sleep(5)
    print('-==-' * 39)
    print('<<< Tente novamente! Talvez você tenha mais sorte!! >>>')

