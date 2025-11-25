#!/usr/bin/env python
"""
Test script to verify that all modules can be imported correctly
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

def test_renderer_creation():
    try:
        print("\nTesting renderer creation...")
        
        import moderngl
        
        # Create a dummy context for testing
        ctx = moderngl.create_standalone_context()
        renderer = Renderer3D(ctx)
        print("✓ Renderer created successfully")
        
        ctx.release()
        print("✓ Context released successfully")
        
        return True
    except Exception as e:
        print(f"✗ Renderer test error: {e}")
        return False

if __name__ == "__main__":
    success = test_imports()
    if success:
        success = test_renderer_creation()
    
    if success:
        print("\n✓ All tests passed!")
    else:
        print("\n✗ Some tests failed!")
        exit(1)