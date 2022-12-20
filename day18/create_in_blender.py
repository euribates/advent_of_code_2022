from random import randrange
import os

import bpy

abspath = os.path.abspath(__file__)
dname = os.path.dirname(os.path.dirname(abspath))



def console_get():
    for area in bpy.context.screen.areas:
        if area.type == 'CONSOLE':
            for space in area.spaces:
                if space.type == 'CONSOLE':
                    return area, space
    return None, None


def console_write(text):
    area, space = console_get()
    if space is None:
        return

    context = bpy.context.copy()
    context.update(dict(
        space=space,
        area=area,
    ))
    for line in text.split("\n"):
        bpy.ops.console.scrollback_append(context, text=line, type='OUTPUT')
        
console_write(dname)
os.chdir(dname)


def load_from_file(filename):
    with open(filename, 'r') as f_input:
        for line in f_input:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            x, y, z = line.split(',')
            yield int(x), int(y), int(z)
        
        
counter = 0
for (x, y, z) in load_from_file('input.txt'):
    cube = bpy.ops.mesh.primitive_cube_add(
        location=(x,y,z),
        scale=(0.45, 0.45, 0.45),
        )
    bpy.ops.object.name = f"cube_{x}_{y}_{z}"
    modifier = bpy.ops.object.modifier_add(type='BEVEL')
    bpy.ops.object.width = 0.01
    counter += 1
    if counter > 100:
        break
