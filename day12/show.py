import random

from PIL import Image, ImageDraw

RED = (255, 99, 99)
GREEN = (99, 255, 99)

SCALE = 25



def left_arrow(im, point, color=(68, 52, 188)):
    left_im = Image.open('left.png')
    x, y = point
    x = x * SCALE
    y = y * SCALE
    im.paste(left_im, (x, y))


def right_arrow(im, point, color=(68, 52, 188)):
    left_im = Image.open('right.png')
    x, y = point
    x = x * SCALE
    y = y * SCALE
    im.paste(left_im, (x, y))


def dot(draw, point, color):
    x, y = point
    offset = SCALE // 5
    box = (
        x * SCALE + offset,
        y * SCALE + offset,
        (x+1) * SCALE - offset,
        (y+1) * SCALE - offset,
    )
    draw.ellipse(box, fill=color)


def box(draw, point, color):
    x, y = point
    offset = SCALE // 10
    box = (
        x * SCALE + offset,
        y * SCALE + offset,
        (x+1) * SCALE - offset,
        (y+1) * SCALE - offset,
    )
    draw.rounded_rectangle(box, radius=2, fill=color)


def create_map_image(node_map, start_at, end_at):
    width, height = max((x, y) for x, y in node_map.keys())
    size = (width * SCALE, height * SCALE)
    im = Image.new('RGB', size, (255, 255, 255))
    draw = ImageDraw.Draw(im)
    for x in range(width):
        for y in range(height):
            value = ord(node_map[x, y]) - 97
            color = (value * 10, value*10, value * 10)
            box(draw, (x, y), color)
    x, y = start_at
    dot(draw, start_at, GREEN)
    dot(draw, end_at, RED)
    left_arrow(im, (3, 3))
    right_arrow(im, (4, 4))
    return im

def show_came_from(node_map, start_at, end_at, came_from):
    pass


if __name__ == '__main__':
    node_map = {}
    for y in range(10):
        for x in range(10):
            node_map[x, y] = random.choice('abcdefghijklmnopqrstuvwxyz')
    start_at = (random.randrange(10), random.randrange(10))
    end_at = (random.randrange(10), random.randrange(10))
    while end_at == start_at:
        end_at = (random.randrange(10), random.randrange(10))
    img = create_map_image(node_map, start_at, end_at)
    img.show()
