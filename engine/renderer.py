"""
OpenGL renderer module for the game engine
"""
import moderngl
import numpy as np
from PIL import Image

class Renderer3D:
    def __init__(self, ctx: moderngl.Context):
        self.ctx = ctx
        self.programs = {}
        self.textures = {}
        self.vao = None
        self.vbo = None
        self.ibo = None
        self.setup_default_geometry()
        self.setup_default_shaders()

    def setup_default_geometry(self):
        """Create default geometry (triangle)"""
        vertices = np.array([
            -0.5, -0.5, 0.0,
            0.5, -0.5, 0.0,
            0.0, 0.5, 0.0
        ], dtype='f4')
        
        indices = np.array([0, 1, 2], dtype='i4')
        
        self.vbo = self.ctx.buffer(vertices.tobytes())
        self.ibo = self.ctx.buffer(indices.tobytes())

    def setup_default_shaders(self):
        """Create default shaders"""
        self.programs['default'] = self.ctx.program(
            vertex_shader='''
                #version 330
                in vec3 in_vert;
                uniform mat4 mvp;
                void main() {
                    gl_Position = mvp * vec4(in_vert, 1.0);
                }
            ''',
            fragment_shader='''
                #version 330
                out vec4 fragColor;
                void main() {
                    fragColor = vec4(0.3, 0.7, 1.0, 1.0);
                }
            '''
        )
        
        self.vao = self.ctx.simple_vertex_array(
            self.programs['default'], 
            self.vbo, 
            'in_vert'
        )

    def render(self):
        """Render the scene"""
        self.ctx.clear(0.1, 0.1, 0.1)
        self.vao.render()
        
    def add_texture(self, name: str, image_path: str):
        """Add a texture from an image file"""
        img = Image.open(image_path).transpose(Image.FLIP_TOP_BOTTOM)
        texture = self.ctx.texture(img.size, 4, img.tobytes())
        texture.build_mipmaps()
        self.textures[name] = texture
        
    def set_uniform(self, program_name: str, uniform_name: str, value):
        """Set a uniform value in a shader program"""
        if program_name in self.programs:
            program = self.programs[program_name]
            if uniform_name in program:
                program[uniform_name].value = value