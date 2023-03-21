# Example file showing a circle moving on screen
import pygame
import numpy as np

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
wide = 40

sisi= 40
centersquare=[screen.get_width()/2,screen.get_height()/2]
a=centersquare[0]-20
b=centersquare[1]+20
c=b-sisi
d=a+sisi
square=[[a,b],[d,b],[a,c],[d,c]]

def rotate_2d_center(vectors, centers, theta):
    vector=np.array(vectors)
    center=np.array(centers)
    # Translasikan titik pusat rotasi ke pusat koordinat
    vector_translated = vector - center
    
    # Lakukan rotasi pada vektor hasil translasi
    rotation_matrix = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
    vector_rotated_translated = np.dot(rotation_matrix, vector_translated)
    
    # Translasikan kembali vektor hasil rotasi ke koordinat asli
    vector_rotated = vector_rotated_translated + center
    
    return vector_rotated


while running:
    
    
    for i in range(len(square)):
        result = rotate_2d_center(square[i], centersquare, np.pi/60)
        square[i][0] = result[0]
        square[i][1] = result[1]
    
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    pygame.draw.line(screen,"white",square[0],square[1])
    pygame.draw.line(screen,"white",square[1],square[3])
    pygame.draw.line(screen,"white",square[2],square[3])
    pygame.draw.line(screen,"white",square[2],square[0]) 
    
    pygame.draw.circle(screen,"white",centersquare,3)   

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        centersquare[1] -= 300 * dt
    if keys[pygame.K_s]:
        centersquare[1] += 300 * dt
    if keys[pygame.K_a]:
        if centersquare[0] > 2:
            centersquare[0] -= 300 * dt
    if keys[pygame.K_d]:
        centersquare[0] += 300 * dt
    if keys[pygame.K_SPACE]:
        wide= wide + (3*dt)


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()