"""
Main application file for the 3D engine
"""
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from engine.renderer import OpenGLViewport
from ui.controls import ControlPanel

class EngineApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("3D Engine")
        self.setGeometry(100, 100, 1200, 800)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        # Создаем OpenGL вьюпорт
        self.viewport = OpenGLViewport(self)
        layout.addWidget(self.viewport)
        
        # Создаем панель управления
        self.controls = ControlPanel(self)
        layout.addWidget(self.controls)

def main():
    app = QApplication(sys.argv)
    engine_app = EngineApp()
    engine_app.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()