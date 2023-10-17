from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from random import randint 
from classes import *
from display import *
import collision_detection as cd

####### GAME CONSTANTS ########################
WINDOW_DIM = 10
STEP = 0.65
SCORE_GOAL = 15
########## ############ #######################
Score = 0
########## PLANE #################
PLAYER_BULLET_SPEED = 0.1
PLANE_DIM = 1  
PLANE_X = 0  
PLANE_Y = -WINDOW_DIM + PLANE_DIM
bullets = []
###################################

########## Alien Variables ################
ALIEN_DIM = 1
ALIEN_N = 5
ALIEN_BULLET_SPEED = 0.03
aliens = []
alienBullets = []
aliensInitPosX = [randint(-WINDOW_DIM + 3, WINDOW_DIM - 3)] 
aliensInitPosY = [randint(0, WINDOW_DIM - 3)]
########## ############ ################

########## STATE VARIABLES ################
shooting = False
attacking = False
losing = False
###############################

############ TEXTURES ##########################
images = ["spaceship.png" , "alien.jpg", "lose.jpg" , "win.jpg","sky.jpg"]
texture_names = [0,1,2 ,3,4]  
def my_init():
    loadTextures(images , texture_names)
##################################################

###### FUNCTIONS ######################
def reset():
    global plane , score
    for alien in aliens:
        genShapePos(alien)
    plane.setX(PLANE_X)
    plane.setY(PLANE_Y)
    alienBullets.clear()
    bullets.clear()
    score = 0

def initShapePos(v):
    for i in range(ALIEN_N):
        rand_x = randint(-WINDOW_DIM + 3, WINDOW_DIM - 3)
        rand_y = randint(-WINDOW_DIM + 3 + PLANE_DIM, WINDOW_DIM - 3)

        while (rand_x in aliensInitPosX) or (rand_x + ALIEN_DIM in aliensInitPosX) or (rand_x - ALIEN_DIM in aliensInitPosX):
            rand_x = randint(-WINDOW_DIM + 3, WINDOW_DIM - 3)

        while (rand_y in aliensInitPosY) or (rand_y + ALIEN_DIM in aliensInitPosY) or (rand_y - ALIEN_DIM in aliensInitPosY):
            rand_y = randint(-WINDOW_DIM + 3 + PLANE_DIM, WINDOW_DIM - 3)

        aliensInitPosX.append(rand_x)
        aliensInitPosY.append(rand_y)

def genShapePos(alien):
    aliensX = [a.getX() for a in aliens ]
    aliensY = [a.getY() for a in aliens ]

    rand_x = randint(-WINDOW_DIM + 3, WINDOW_DIM - 3)
    rand_y = randint(-WINDOW_DIM + 3 + PLANE_DIM, WINDOW_DIM - 3)
    
    while (rand_x in aliensX) or (rand_x + ALIEN_DIM in aliensX) or (rand_x - ALIEN_DIM in aliensX):
        rand_x = randint(-WINDOW_DIM + 3, WINDOW_DIM - 3)

    while (rand_y in aliensY) or (rand_y + ALIEN_DIM in aliensY) or (rand_y - ALIEN_DIM in aliensY):
        rand_y = randint(-WINDOW_DIM + 3 + PLANE_DIM, WINDOW_DIM - 3)
     
    alien.setY(rand_y)
    alien.setX(rand_x)

initShapePos(ALIEN_N)
################################################

###### INIT PLANE AND ALIENS #################
plane = SpaceShip(PLANE_DIM , PLANE_X , PLANE_Y)
for i in range(ALIEN_N):
    aliens.append(SpaceShip(ALIEN_DIM , aliensInitPosX[i] , aliensInitPosY[i]))
#################################################

def mainFunc():
    global plane, aliens, alienBullets, bullets,  shooting , attacking , losing , Score

    glClearColor(1,1,1,1)
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-WINDOW_DIM, WINDOW_DIM, -WINDOW_DIM, WINDOW_DIM) 

    if not losing and Score != SCORE_GOAL:
        drawScreen(texture_names[4],WINDOW_DIM)
        drawChar("Score: " + str(Score) + "/" + str(SCORE_GOAL), -WINDOW_DIM + 0.5, WINDOW_DIM - 1)
       

        # Collision Detection (Player bullet vs alien)
        for b in bullets:
            for alien in aliens:
                if cd.test_alien_bullet(alien ,b):
                    genShapePos(alien)
                    Score += 1
                    b.remove()

        # Collision Detection (alien bullet vs player)
        for b in alienBullets:
            if cd.test_plane_bullet(plane , b):
                losing = True

        # Collision Detection (alien vs player)
        for alien in aliens:
            if cd.test_alien_plane(alien , plane):
                losing = True        
        
        # Collision Detection (Plane vs Wall)
        cd.test_plane_wall(plane , WINDOW_DIM)
        
        if shooting:           
            for b in bullets:
                b.shoot()
                if b.BulletY > WINDOW_DIM:
                    bullets.remove(b)
  
        if attacking:
            for b in alienBullets:
                b.shoot()
                if b.BulletY < -WINDOW_DIM:
                    alienBullets.remove(b)

        glColor3f(1, 1, 1)
        glPushMatrix()
        glTranslate(plane.getX(), plane.getY(), 0)        
        plane.draw(texture_names[0])
        glPopMatrix()

        for alien in aliens:
            glPushMatrix()
            glTranslate(alien.getX(), alien.getY(), 0)
            alien.draw(texture_names[1])
            glPopMatrix()

    else:
        if losing:
            drawScreen(texture_names[2] , WINDOW_DIM)
            Score = 0
        else:
            drawScreen(texture_names[3] , WINDOW_DIM)  

    glutSwapBuffers()    

def keyboard(key , x , y):
    global  bullets , plane , losing , shooting 
    if key == b"d":
        plane.moveRight(STEP)

    if key == b"a":
        plane.moveLeft(STEP)

    if key == b"w":
        plane.moveUp(STEP)

    if key == b"s":
        plane.moveDown(STEP)

    if key == b"k":
        bullets.append(Bullet(plane.getX(),plane.getY(), 3 , PLAYER_BULLET_SPEED))
        shooting = True 

    if key == b"q":
        glutDestroyWindow()

    if key == b"r" and losing:
        losing = False
        reset()    

def Repeat(v):
    global alienBullets ,AlienBulletX, AlienBulletY, attacking
    mainFunc()        

    if v == 1000:
        attacking = True
        for alien in aliens:
            alienBullets.append(Bullet(alien.getX() , alien.getY(),5 , ALIEN_BULLET_SPEED , False))
        v = 0

    glutTimerFunc(1 , Repeat , v + 1)    

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowPosition(300, 20)
glutInitWindowSize(650, 650)
glutCreateWindow(b"Aliens Invasion")
my_init()
glutDisplayFunc(mainFunc)
glutTimerFunc(100, Repeat, 1)
glutKeyboardFunc(keyboard)
glutMainLoop()