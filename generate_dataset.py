# Генерация датасета
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import drawsvg as draw
import random
import os

class Sample: 
    pass

class CircleInfo:
    def __init__(self, cx, cy, r):
        self.cx = cx
        self.cy = cy
        self.r = r

    def __str__(self):
        return "(cx: {}, cy: {}, r: {})".format(self.cx, self.cy, self.r)

    def __repr__(self):
        return "(cx: {}, cy: {}, r: {})".format(self.cx, self.cy, self.r)

# Draw test circle
def is_intersect(cx, cy, r, circles):
    for circle in circles:
        rr = r + circle.r
        dx = cx - circle.cx
        dy = cy - circle.cy
        if (rr * rr > dx * dx + dy * dy):
            return True
    return False

Sample.width = 32
Sample.height = 32
Sample.count = 1
Sample.max_radius = 14

def create_image(file_name_index):
    d = draw.Drawing(Sample.width, Sample.height, origin='top-left')
    # Draw a rectangle
    r = draw.Rectangle(0, 0, Sample.width, Sample.height, fill='white')
    d.append(r)
    circles = []
    for _ in range(Sample.count):
        while True:
            r = random.randint(1, Sample.max_radius)
            cx = random.randint(r, Sample.width - r)
            cy = random.randint(r, Sample.height - r)
            if not is_intersect(cx, cy, r, circles):
                break
        circles.append(CircleInfo(cx, cy, r))
        d.append(draw.Circle(cx, cy, r, fill='black', stroke_width=0, stroke='black'))
    d.set_pixel_scale(1)  # Set number of pixels per geometry unit
    d.save_png('data/img/' + file_name_index + '.png')
    return circles

def gen_n_images(n):
    os.makedirs("data/img", exist_ok=True)
    lines = []
    for file_index_name in range(1, n + 1):
        circles = create_image(f"{file_index_name:05}")
        lines.append(f"{file_index_name:05}, {circles[0].cx}, {circles[0].cy}, {circles[0].r}")
    with open("data/output.txt", "w") as file:
        for line in lines:
            file.write(line + "\n")

gen_n_images(100)
