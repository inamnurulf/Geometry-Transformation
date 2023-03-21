import pygame
import numpy as np
import random

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

sisi= 80
centersquare=[screen.get_width()/2,screen.get_height()/2]
a=centersquare[0]-40
b=centersquare[1]+40
c=b-sisi
d=a+sisi
square=[[a,b],[d,b],[a,c],[d,c]]

randomdot=[screen.get_width()/2+50,screen.get_height()/2+50]

font = pygame.font.SysFont("Arial", 30)

number = 0

def rotate_2d_center(vectors, centers, theta):
    vector=np.array(vectors)
    center=np.array(centers)

    vector_translated = vector - center
    
    rotation_matrix = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
    vector_rotated_translated = np.dot(rotation_matrix, vector_translated)
    
    vector_rotated = vector_rotated_translated + center
    
    return vector_rotated

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
    
def is_cube_out_of_bounds(cube, screen_width, screen_height):
    for point in cube:
        if point[0] < 0 or point[0] > screen_width or point[1] < 0 or point[1] > screen_height:
            return True
    return False



while running:
    
    if(is_cube_out_of_bounds(square,screen.get_width(),screen.get_height())==True):
        a=centersquare[0]-40
        b=centersquare[1]+40
        c=b-sisi
        d=a+sisi
        square=[[a,b],[d,b],[a,c],[d,c]]
        number =0
        
    
    for i in range(len(square)):
        result = rotate_2d_center(square[i], centersquare, np.pi/60)
        square[i][0] = result[0]
        square[i][1] = result[1]
    
    centerscale=[(square[0][0]+square[2][0])/2,(square[0][1]+square[2][1])/2]
    
    if (is_dot_inside_square(randomdot,square)==True):
        randomdot=[random.randint(30,screen.get_width()/2-50),random.randint(30,screen.get_height()/2-50)]
        for i in range(len(square)):
            result = scale_point(square[i], centerscale, 4/5)
            square[i][0] = result[0]
            square[i][1] = result[1]
        number+=1
   
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    
    info_text = font.render("Hit the 'red' dot with the 'square'", True, (255, 255, 255))
    info_rect = info_text.get_rect()
    info_rect.bottomright = (screen.get_width()/2+50, screen.get_height())
    screen.blit(info_text, info_rect)
    

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

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()