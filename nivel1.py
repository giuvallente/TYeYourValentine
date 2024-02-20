import pygame
import numpy as np

pygame.init()

# Tamanho da tela e definição do FPS
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()
FPS = 60  # Frames per Second

BLACK = (0, 0, 0)
COR_PERSONAGEM = (30, 200, 20)
COR_PREMIO = (255, 255, 0)
COR_PLANETA = (255, 0, 0)

# Inicializar posicoes
s0 = np.array([50,200])
v0 = np.array([0, 0])
a = np.array([0, 0.2])
v = v0
s = s0

# Personagem
personagem = pygame.Surface((5, 5))  # Tamanho do personagem
personagem.fill(COR_PERSONAGEM)  # Cor do personagem

clicou = False

rodando = True
while rodando:
    # Capturar eventos

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos_mouse = event.pos
            v = (pos_mouse - s0) * 1/np.linalg.norm(pos_mouse - s0)
            v = v * 10 
            clicou = True
            

    if s[0]<10 or s[0]>390 or s[1]<10 or s[1]>390: # Se eu chegar ao limite da tela, reinicio a posição do personagem
        v = (pos_mouse - s0) * 1/np.linalg.norm(pos_mouse - s0)
        v = v * 10
        s, v = s0, v
        clicou = False

    # Controlar frame rate
    clock.tick(FPS)

    # Processar posicoes
    pos_planeta = np.array([300, 100])

    if clicou:

        vetor = (pos_planeta - s) * 1/np.linalg.norm(pos_planeta - s) 
        a = (1000 / (np.linalg.norm(pos_planeta - s)) ** 2) * vetor
        v = v + a 
        s = s + 0.1 * v 

    # Desenha fundo
    screen.fill(BLACK)

    # Desenha planeta
    pygame.draw.circle(screen, COR_PLANETA, (300, 100), 20, 1)

    # Desenha prêmio
    pygame.draw.circle(screen, COR_PREMIO, (350, 200), 10, 1)

    # Desenha personagem
    rect = pygame.Rect(s, (10, 10))  # First tuple is position, second is size.
    screen.blit(personagem, rect)

    # Update!
    pygame.display.update()

# Terminar tela
pygame.quit()