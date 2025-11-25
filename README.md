# 3D Game Engine

A custom 3D game engine built with Python using ModernGL for rendering and PyQt5 for the user interface.

## Features

- OpenGL 3.3+ rendering with ModernGL
- Real-time 3D viewport
- UI control panel with Qt
- Modular architecture
- Extensible shader system

## Requirements

- Python 3.7+
- ModernGL
- PyQt5
- NumPy
- Pillow

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

## Architecture

- `main.py` - Main application entry point
- `engine/` - Core engine components
  - `renderer.py` - OpenGL rendering system
- `ui/` - User interface components
  - `controls.py` - Control panel UI

## Current Status

This is a basic implementation showing:
- OpenGL context initialization
- Basic triangle rendering
- Qt-based control panel
- Modular architecture for expansion

## Next Steps

- Add 3D model loading
- Implement camera system
- Add lighting and materials
- Create scene graph
- Add input handling
- Implement post-processing effects