import pygame
import random
pygame.init()

width = 1280
height = 720

display_surface = pygame.display.set_mode((width, height))

pygame.display.set_caption('Mygame')

surf = pygame.Surface((100, 100))
surf.fill((255, 0, 0))

player_surf = pygame.image.load('images/player.png').convert_alpha()
player_rect = player_surf.get_rect(center=(width/2, height/2))
star_surf = pygame.image.load('images/star.png').convert_alpha()

star_positions = [(random.randint(0, width), random.randint(0, height)) for _ in range(20)]


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
    display_surface.fill(('darkgray'))
    
    for star_position in star_positions:
        display_surface.blit(star_surf, star_position)
    if player_rect.right < width:
        player_rect.right += 1
    else:
        player_rect.left = 0
    
    display_surface.blit(player_surf, player_rect)
    
    pygame.display.update()
