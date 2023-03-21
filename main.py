# Example file showing a circle moving on screen
import pygame
import numpy as np
import random

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

randomdot=[screen.get_width()/2+50,screen.get_height()/2+50]

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

font = pygame.font.SysFont("Arial", 30)

# variable setup
number = 0
def scale_point(point, center, scale_factor):
    x = center[0] + scale_factor * (point[0] - center[0])
    y = center[1] + scale_factor * (point[1] - center[1])
    return [x, y]

def is_dot_inside_square(dot, square):
    min_x = min(square[0][0], square[1][0], square[2][0], square[3][0])
    max_x = max(square[0][0], square[1][0], square[2][0], square[3][0])
    min_y = min(square[0][1], square[1][1], square[2][1], square[3][1])
    max_y = max(square[0][1], square[1][1], square[2][1], square[3][1])

    if dot[0] >= min_x and dot[0] <= max_x and dot[1] >= min_y and dot[1] <= max_y:
        return True
    else:
        return False


while running:
    
    for i in range(len(square)):
        result = rotate_2d_center(square[i], centersquare, np.pi/60)
        square[i][0] = result[0]
        square[i][1] = result[1]
    
    centerscale=[(square[0][0]+square[2][0])/2,(square[0][1]+square[2][1])/2]
    
    if (is_dot_inside_square(randomdot,square)==True):
        randomdot=[random.randint(30,screen.get_width()/2-50),random.randint(30,screen.get_height()/2-50)]
        for i in range(len(square)):
            result = scale_point(square[i], centerscale, 9/10)
            square[i][0] = result[0]
            square[i][1] = result[1]
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    number_text = font.render(str(number), True, (255, 255, 255))
    number_rect = number_text.get_rect()
    number_rect.bottomright = (screen.get_width() - 10, screen.get_height() - 10)
    screen.blit(number_text, number_rect)
    
    pygame.draw.line(screen,"white",square[0],square[1])
    pygame.draw.line(screen,"white",square[1],square[3])
    pygame.draw.line(screen,"white",square[2],square[3])
    pygame.draw.line(screen,"white",square[2],square[0]) 
    
    pygame.draw.circle(screen,"white",centersquare,3) 
    pygame.draw.circle(screen,"red",randomdot,3)  

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