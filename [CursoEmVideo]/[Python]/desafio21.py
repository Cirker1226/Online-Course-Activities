import pygame
pygame.init()

# Carrega o arquivo de áudio

pygame.mixer.music.load(r'c:\Users\mathe\Downloads\[Programação]\[CursoEmVideo]\[Python]\CuidaBem.mp3')

# Reproduz o áudio 

pygame.mixer.music.play()

# Aguarda o término do evento

pygame.event.wait()