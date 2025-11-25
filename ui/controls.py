"""
UI controls for the game engine
"""
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, 
    QLabel, QSlider, QGroupBox, QGridLayout
)
from PyQt5.QtCore import Qt

class EngineControlPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        layout = QVBoxLayout()
        
        # Create main control group
        controls_group = QGroupBox("Engine Controls")
        controls_layout = QGridLayout()
        
        # Add some basic controls
        self.add_render_button = QPushButton("Render Frame")
        self.add_render_button.clicked.connect(self.on_render_clicked)
        
        self.clear_button = QPushButton("Clear Viewport")
        self.clear_button.clicked.connect(self.on_clear_clicked)
        
        # Add sliders for camera controls
        self.cam_x_slider = self.create_slider("Camera X", -100, 100)
        self.cam_y_slider = self.create_slider("Camera Y", -100, 100)
        self.cam_z_slider = self.create_slider("Camera Z", -100, 100)
        
        # Add to grid
        controls_layout.addWidget(self.add_render_button, 0, 0)
        controls_layout.addWidget(self.clear_button, 0, 1)
        controls_layout.addWidget(self.cam_x_slider['label'], 1, 0)
        controls_layout.addWidget(self.cam_x_slider['slider'], 1, 1)
        controls_layout.addWidget(self.cam_y_slider['label'], 2, 0)
        controls_layout.addWidget(self.cam_y_slider['slider'], 2, 1)
        controls_layout.addWidget(self.cam_z_slider['label'], 3, 0)
        controls_layout.addWidget(self.cam_z_slider['slider'], 3, 1)
        
        controls_group.setLayout(controls_layout)
        layout.addWidget(controls_group)
        
        # Add status display
        self.status_label = QLabel("Ready")
        layout.addWidget(self.status_label)
        
        self.setLayout(layout)
        
    def create_slider(self, label_text, min_val, max_val):
        """Create a labeled slider"""
        container = QWidget()
        layout = QHBoxLayout()
        
        label = QLabel(label_text)
        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(min_val)
        slider.setMaximum(max_val)
        slider.setValue(0)
        
        layout.addWidget(label)
        layout.addWidget(slider)
        container.setLayout(layout)
        
        return {'label': label, 'slider': slider, 'container': container}
        
    def on_render_clicked(self):
        """Handle render button click"""
        self.status_label.setText("Rendering...")
        
    def on_clear_clicked(self):
        """Handle clear button click"""
        self.status_label.setText("Viewport cleared")
        
    def get_camera_position(self):
        """Get camera position from sliders"""
        x = self.cam_x_slider['slider'].value() / 10.0
        y = self.cam_y_slider['slider'].value() / 10.0
        z = self.cam_z_slider['slider'].value() / 10.0
        return (x, y, z)