import pygame

pygame.mixer.init()

pygame.mixer.music.load('Metallica - Nothing Else Matters.mp3')

pygame.mixer.music.play()

input('Aperte Enter para parar a música...')
