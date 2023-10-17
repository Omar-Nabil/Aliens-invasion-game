from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import pygame


def texture_setup(texture_image_binary, texture_name, width, height):
    glBindTexture(GL_TEXTURE_2D, texture_name)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

    glTexImage2D(GL_TEXTURE_2D,
                 0,  # mipmap
                 3,  # Bytes per pixel
                 width, height,
                 0,  # Texture border
                 GL_RGBA,  # RGBA Exactly as in  pygame.image.tostring(image, "RGBA", True)
                 GL_UNSIGNED_BYTE,
                 texture_image_binary)  # texture init STEP [7]


def loadTextures(imagesList , names):

    glEnable(GL_TEXTURE_2D)
    glEnable(GL_BLEND)  # FOR BLENDING
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)  # FOR BLENDING
    images = []
    for img in imagesList:
        images.append(pygame.image.load(img))
   
    textures = [pygame.image.tostring(image, "RGBA", True)
                for image in images]

    glGenTextures(len(images), names)

    for i in range(len(images)):
        texture_setup(textures[i],
                      names[i],
                      images[i].get_width(),
                      images[i].get_height())

def drawScreen(texture , dim):
    glColor3f(1, 1, 1)

    glBindTexture(GL_TEXTURE_2D, texture)  # Binding The Plane Texture No. 2
    glBegin(GL_QUADS)

    glTexCoord2f(0, 0)
    glVertex2f(-dim, -dim)

    glTexCoord2f(0, 1)
    glVertex2f(-dim, dim)

    glTexCoord2f(1, 1)
    glVertex2f(dim, dim)

    glTexCoord2f(1, 0)
    glVertex2f(dim, -dim)

    glEnd()

def drawChar(string, x, y):
    glLineWidth(2)
    glColor(0, 0,0)
    glPushMatrix()  # remove the previous transformations
    glTranslate(x, y, 0)
    glScale(0.0045, 0.0045, 1)  # DownScale According To Our Dimensions
    string = string.encode()
    for c in string:
        glutStrokeCharacter(GLUT_STROKE_ROMAN, c)
    glPopMatrix()    