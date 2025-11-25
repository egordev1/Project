"""
Main application file for the game engine
"""
import sys
import moderngl
from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QWidget, QOpenGLWidget
from PyQt5.QtCore import QTimer
from engine.renderer import Renderer3D
from ui.controls import EngineControlPanel

class OpenGLViewport(QOpenGLWidget):
    def __init__(self):
        super().__init__()
        self.ctx = None
        self.renderer = None

    def initializeGL(self):
        # Initialize ModernGL context from the existing OpenGL context
        self.ctx = moderngl.create_context(require=330)
        self.renderer = Renderer3D(self.ctx)

    def paintGL(self):
        if self.renderer:
            self.renderer.render()

    def resizeGL(self, width, height):
        if self.ctx:
            self.ctx.viewport = (0, 0, width, height)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Game Engine")
        self.setGeometry(100, 100, 1200, 800)
        
        # Main widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QHBoxLayout(central_widget)
        
        # Add the OpenGL viewport
        self.viewport = OpenGLViewport()
        layout.addWidget(self.viewport, 4)  # 4/5 of the space
        
        # Add the control panel
        self.controls = EngineControlPanel()
        layout.addWidget(self.controls, 1)  # 1/5 of the space
        
        # Timer for updating the viewport
        self.timer = QTimer()
        self.timer.timeout.connect(self.viewport.update)
        self.timer.start(16)  # ~60 FPS

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()