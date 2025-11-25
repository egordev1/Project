#!/usr/bin/env python
"""
Test script to verify that all modules can be imported correctly without requiring a display
"""

def test_imports():
    try:
        print("Testing imports...")
        
        import moderngl
        print("✓ moderngl imported successfully")
        
        import PyQt5
        print("✓ PyQt5 imported successfully")
        
        import numpy as np
        print("✓ numpy imported successfully")
        
        from PIL import Image
        print("✓ PIL imported successfully")
        
        from engine.renderer import Renderer3D
        print("✓ engine.renderer imported successfully")
        
        from ui.controls import EngineControlPanel
        print("✓ ui.controls imported successfully")
        
        print("\nAll modules imported successfully!")
        return True
        
    except ImportError as e:
        print(f"✗ Import error: {e}")
        return False

def test_class_creation():
    """Test that classes can be defined without requiring a display"""
    try:
        print("\nTesting class definitions...")
        
        # Test that we can reference the classes without instantiating them
        from engine.renderer import Renderer3D
        from ui.controls import EngineControlPanel
        
        print("✓ Classes can be referenced without instantiation")
        
        # Test that we can create instances of UI controls without a full Qt app
        import sys
        from PyQt5.QtWidgets import QApplication
        
        # Create a minimal QApplication for testing
        if not QApplication.instance():
            app = QApplication(sys.argv)
        
        control_panel = EngineControlPanel()
        print("✓ UI control panel created successfully")
        
        # Test that renderer class can be referenced
        print("✓ Renderer class can be referenced")
        
        print("✓ All class tests passed")
        return True
    except Exception as e:
        print(f"✗ Class test error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_imports()
    if success:
        success = test_class_creation()
    
    if success:
        print("\n✓ All tests passed!")
    else:
        print("\n✗ Some tests failed!")
        exit(1)