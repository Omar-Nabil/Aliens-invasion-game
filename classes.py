from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


class Bullet:
    def __init__(self , x , y ,size, offset , up = True):
        self.BulletX = x
        self.BulletY = y
        self.size = size
        if up:
            self.offset = offset
        else:
            self.offset = -offset    

    def shoot(self):
        self.BulletY += self.offset
        glPointSize(self.size)
        glBegin(GL_POINTS)
        glColor(0,0,0)
        glVertex(self.BulletX, self.BulletY)
        glEnd()

    def remove(self):
        self.BulletX = 500
        self.BulletY = 500
        
class SpaceShip:
    def __init__(self ,dim, x , y):
        self.dim = dim
        self.x = x
        self.y = y   

    def getX(self):
        return self.x      

    def getY(self):
        return self.y      

    def setX(self , val):
        self.x = val   

    def setY(self , val):
        self.y = val    

    def moveRight(self , step):
        self.x += step

    def moveLeft(self , step):
        self.x -= step

    def moveUp(self , step):
        self.y += step

    def moveDown(self , step):
        self.y -= step        

    def draw(self , texture):
        glBindTexture(GL_TEXTURE_2D, texture)  # Binding The Plane Texture No. 0
        glBegin(GL_QUADS)

        glTexCoord2f(0, 0)
        glVertex2f(-self.dim, -self.dim)

        glTexCoord2f(0, 1)
        glVertex2f(-self.dim, self.dim)

        glTexCoord2f(1, 1)
        glVertex2f(self.dim, self.dim)

        glTexCoord2f(1, 0)
        glVertex2f(self.dim, -self.dim)    
        glEnd()
        glBindTexture(GL_TEXTURE_2D, -1)

########## ############ #######################