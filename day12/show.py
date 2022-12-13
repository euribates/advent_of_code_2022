from functools import partial
import random

from PIL import Image, ImageDraw

RED = (255, 99, 99)
GREEN = (99, 255, 99)

SCALE = 25



def paste_img(im, point, filename=''):
    sub_im = Image.open(filename)
    x, y = point
    x = x * SCALE
    y = y * SCALE
    im.alpha_composite(sub_im, (x, y))
    return im


left_arrow = partial(paste_img, filename='left.png')
right_arrow = partial(paste_img, filename='right.png')
up_arrow = partial(paste_img, filename='up.png')
down_arrow = partial(paste_img, filename='down.png')


def dot(draw, point, color=GREEN):
    x, y = point
    offset = SCALE // 5
    box = (
        x * SCALE + offset,
        y * SCALE + offset,
        (x+1) * SCALE - offset,
        (y+1) * SCALE - offset,
    )
    draw.ellipse(box, fill=color)


def box(draw, point, color=RED):
    x, y = point
    offset = SCALE // 10
    box = (
        x * SCALE + offset,
        y * SCALE + offset,
        (x+1) * SCALE - offset,
        (y+1) * SCALE - offset,
    )
    draw.rounded_rectangle(box, radius=2, fill=color)


def create_map_image(width, height, node_map, start_at, end_at):
    size = (width * SCALE, height * SCALE)
    im = Image.new('RGBA', size, (255, 255, 255))
    draw = ImageDraw.Draw(im)
    for x in range(width):
        for y in range(height):
            value = ord(node_map[x, y]) - 97
            color = (value * 10, value*10, value * 10)
            box(draw, (x, y), color)
    x, y = start_at
    dot(draw, start_at, GREEN)
    dot(draw, end_at, RED)
    return im


def show_came_from(width, height, node_map, start_at, end_at, came_from):
    im = create_map_image(width, height, node_map, start_at, end_at)
    for x0 in range(width):
        for y0 in range(height):
            if (x0, y0) in came_from:
                p = came_from[(x0, y0)]
                if p is None:
                    continue
                (x1, y1) = p
                match (x0-x1, y0-y1):
                    case (0, 1):
                        im = up_arrow(im, (x0, y0))
                    case (0, -1):
                        im = down_arrow(im, (x0, y0))
                    case (1, 0):
                        im = left_arrow(im, (x0, y0))
                    case (-1, 0):
                        im = right_arrow(im, (x0, y0))
                    case _:
                        raise ValueError(
                            f'Algo fue fatal {x0=},{y0=} -> {x1=},{y1=}'
                            f' {x0-x1, y0-y1}'
                            )
    return im


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
    came_from = {
        (4, 4): (4, 3),
        (4, 3): (3, 3),
        (3, 3): (3, 4),
        (3, 4): (3, 5),
        (3, 5): (3, 6),
        (3, 6): (4, 6),
        }
    img = show_came_from(node_map, start_at, end_at, came_from)
    img.show()
