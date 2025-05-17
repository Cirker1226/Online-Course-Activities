import os
os.system('cls' if os.name == 'nt' else 'clear')

import pygame
pygame.init()

# Obtém o diretório onde está o script
diretorio = os.path.dirname(os.path.abspath(__file__))

# Monta o caminho completo do arquivo de áudio
caminho_musica = os.path.join(diretorio, 'CuidaBem.mp3')

pygame.mixer.music.load(caminho_musica)
pygame.mixer.music.set_volume(0.5)  # Define o volume (0.0 a 1.0)
pygame.mixer.music.play()

print("-"*80, "\n")
input("Pressione Enter para sair...")
print("-"*80)

# Para tocar é necessario ter um arquivo .mp3 salvo no mesmo diretorio que o arquivo pertence.
