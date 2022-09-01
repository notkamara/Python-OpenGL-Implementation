import pygame, math
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

fps = 30

clock = pygame.time.Clock()

width = 800.0
height = 450.0

cameraPos = (0,0,0)

cameraX = 0
cameraY = 0
cameraZ = 0

cameraVX = 0
cameraVY = 0
cameraVZ = 0

camRotX = 0
camRotY = 0
camRotZ = 0

mouseVec = (0,0)
mouseVX = 0
mouseVY = 0

vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    )

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )


pygame.init()
display = (int(width), int(height))
pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

gluPerspective(90, float(width/height), 0.1, 50.0)

glTranslatef(0.0,0.0, -5)

pygame.mouse.set_visible(False)
pygame.event.set_grab(1)


def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == KEYDOWN:
            if event.key == K_w:
                cameraVZ = -0.5
            elif event.key == K_s:
                cameraVZ = 0.5
            elif event.key == K_a:
                cameraVX = -0.5
            elif event.key == K_d:
                cameraVX = 0.5
            elif event.key == K_SPACE:
                cameraVY = 0.5
            elif event.key == K_c:
                cameraVY = -0.5
            elif event.key == K_ESCAPE:
                pygame.quit()
                quit()
        if event.type == KEYUP:
            if event.key == K_w:
                cameraVX = 0
                cameraVZ = 0
            elif event.key == K_s:
                cameraVX = 0                
                cameraVZ = 0
            elif event.key == K_a:
                cameraVX = 0
            elif event.key == K_d:
                cameraVX = 0
            elif event.key == K_SPACE:
                cameraVY = 0
            elif event.key == K_c:
                cameraVY = 0
    mouseVector = pygame.mouse.get_rel()
    mouseVX, mouseVY = mouseVector

    camRotX -= mouseVY
    camRotY += mouseVX

    if camRotX < -90:
        camRotX = -90
    elif camRotX > 90:
        camRotX = 90

    if camRotY <= -180:
        camRotY += 360
    elif camRotY > 180:
        camRotY -= 360
    
    cameraX += cameraVZ * math.sin(math.radians(camRotY)) + cameraVX * math.cos(math.radians(camRotY))
    cameraY += cameraVY
    cameraZ += cameraVZ * math.cos(math.radians(camRotY)) - cameraVX * math.sin(math.radians(camRotY))
    
    glRotatef(mouseVX, 1, 0, 0)
    glRotatef(-mouseVY, 0, 1, 0)
    glRotatef(camRotZ, 0, 0, 1)
    
    glTranslatef(-cameraVX, -cameraVY, -cameraVZ)
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    Cube()
    pygame.display.flip()
    clock.tick(fps)


