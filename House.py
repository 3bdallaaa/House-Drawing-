# Mohamed Abdalla

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import numpy as np

def myInit():
    glClearColor(0.5, 0.9, 1.0, 1.0) #Blue color (Sky)
    gluOrtho2D(0, 500, 500, 0) 

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(1.0, 0.9, 0.0) #Yellow circle (sun)
    x_centre = 462
    y_centre = 38
    r = 35
    glVertex2f(x_centre, y_centre)
    for theta in np.arange(0, 2*math.pi + 0.1, 0.1):
        x = r*math.cos(theta)
        y = r*math.sin(theta)
        glVertex2f(x + x_centre, y + y_centre)
    glEnd()
    
    glColor3f(0.9, 0.8, 0.6)  #Sand color
    glRectf(0, 250, 500, 500) #(left,up,right,down)
    
    glColor3f(0.8, 0.4, 0.1) #Brown color (House)
    glRectf(50, 300, 210 , 460)
    
    glColor3f(0, 0, 0) #Black color (Door)
    glRectf(135, 380, 190 , 460)
    
    glColor3f(0.5, 0.5, 0.5) #Gray color (Window)
    glRectf(65, 325, 110 , 370)
    
    glColor3f(0.8, 0.3, 0.2) #Red Triangle (Roof)
    glBegin(GL_TRIANGLES)
    glVertex2f(210, 300) #Right point
    glVertex2f(50, 300)  #Left point
    glVertex2f(130, 215) #upper point
    glEnd()
    
    glColor3f(1.0, 0.9, 0.0) #Yellow lines (Sun Rays)
    glLineWidth(4) # Increase line size
    glBegin(GL_LINES)
    glVertex2f(430, 27) # --> line 1
    glVertex2f(380, 38) # <--
    glVertex2f(430, 48) # --> line 2
    glVertex2f(385, 67) # <--
    glVertex2f(440, 65) # --> line 3
    glVertex2f(400, 95) # <--
    glVertex2f(460, 70) # --> line 4
    glVertex2f(435,115) # <--
    glEnd()
    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(450, 100)
glutCreateWindow("House")

myInit()
glutDisplayFunc(display)
glutMainLoop()
