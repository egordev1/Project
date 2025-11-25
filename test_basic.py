#!/usr/bin/env python
"""
Basic test script to verify that all modules can be imported correctly
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
        
        # Test that we can access class attributes without instantiation
        print(f"✓ Renderer3D class: {Renderer3D.__name__}")
        print(f"✓ EngineControlPanel class: {EngineControlPanel.__name__}")
        
        print("\nAll modules imported successfully!")
        return True
        
    except ImportError as e:
        print(f"✗ Import error: {e}")
        return False

if __name__ == "__main__":
    success = test_imports()
    
    if success:
        print("\n✓ All tests passed!")
    else:
        print("\n✗ Some tests failed!")
        exit(1)