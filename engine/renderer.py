"""
OpenGL renderer module for the 3D engine
"""
from PyQt5.QtWidgets import QOpenGLWidget
from PyQt5.QtCore import Qt
from PyQt5.QtOpenGL import QGLFormat
import OpenGL.GL as gl
import numpy as np
from PIL import Image

class OpenGLViewport(QOpenGLWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Устанавливаем формат OpenGL
        format = QGLFormat()
        format.setVersion(3, 3)
        format.setProfile(QGLFormat.CoreProfile)
        format.setDepth(24)
        format.setDoubleBuffer(True)
        self.setFormat(format)
        
        self.vertices = np.array([
            -0.5, -0.5, 0.0,
            0.5, -0.5, 0.0,
            0.0, 0.5, 0.0
        ], dtype=np.float32)
        
    def initializeGL(self):
        """Инициализация OpenGL контекста"""
        gl.glEnable(gl.GL_DEPTH_TEST)
        gl.glClearColor(0.1, 0.1, 0.1, 1.0)
        
    def paintGL(self):
        """Рендеринг сцены"""
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
        
        # Устанавливаем цвет
        gl.glColor3f(0.3, 0.7, 1.0)
        
        # Рендерим треугольник
        gl.glBegin(gl.GL_TRIANGLES)
        for i in range(0, len(self.vertices), 3):
            gl.glVertex3f(self.vertices[i], self.vertices[i+1], self.vertices[i+2])
        gl.glEnd()
        
    def resizeGL(self, width, height):
        """Обработка изменения размера вьюпорта"""
        gl.glViewport(0, 0, width, height)