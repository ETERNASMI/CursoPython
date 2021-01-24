from random import choice
import time
PEDRA = 'PEDRA'
PAPEL = 'PAPEL'
TESOURA = 'TESOURA'
es = [PEDRA, PAPEL, TESOURA]
pe = choice(es)
print('===='*39)
pl = input('Vamos Jogar JOKENPO!!\nEscolha entre PEDRA , PAPEL e TEROUSA ')
print('====' * 39)
print('PREPARANDO!!? 1,2,3...')
time.sleep(2)
print('====' * 39)
print('Você jogou {} e Eu {}'.format(pl, pe))
time.sleep(2)
if pl == PEDRA:
    if pe == PEDRA:
        print('====' * 39)
        print('Jogo EMPATADO!!')
        print('====' * 39)
    if pe == PAPEL:
        print('====' * 39)
        print('Você PERDEU!!')
        print('====' * 39)
    if pe == TESOURA:
        print('====' * 39)
        print('Você VENCEU!! PARABENS!!')
        print('====' * 39)
elif pl == PAPEL:
    if pe == PAPEL:
        print('====' * 39)
        print('Jogo EMPATADO!!')
        print('====' * 39)
    if pe == PEDRA:
        print('====' * 39)
        print('Você VENCEU!! PARABENS!!')
        print('====' * 39)
    if pe == TESOURA:
        print('====' * 39)
        print('Você PERDEU!!')
        print('====' * 39)
elif pl == TESOURA:
    if pe == TESOURA:
        print('====' * 39)
        print('Jogo EMPATADO!!')
        print('====' * 39)
    if pe == PEDRA:
        print('====' * 39)
        print('Você PERDEU!!')
        print('====' * 39)
    if pe == PAPEL:
        print('====' * 39)
        print('Você VENCEU!! PARABENS!!')
        print('====' * 39)

