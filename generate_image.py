import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import drawsvg as draw
import random

class sample: 
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
        
sample.width = 640
sample.height = 640
sample.count = 5

d = draw.Drawing(sample.width, sample.height, origin='top-left')

# # Draw an irregular polygon
# d.append(draw.Lines(-80, 45,
#                      70, 49,
#                      95, -49,
#                     -90, -40,
#                     close=False,
#             fill='#eeee00',
#             stroke='black'))

# # Draw a rectangle
r = draw.Rectangle(0, 0, sample.width, sample.height, fill='white')
# r.append_title("Our first rectangle")  # Add a tooltip
d.append(r)

# Draw test circle
def is_intersect(cx, cy, r, circles):
        for circle in circles:
                rr = r + circle.r
                dx = cx - circle.cx
                dy = cy - circle.cy
                if ( rr*rr > dx*dx + dy*dy):
                        return True
        return False


circles = []
for n in range(sample.count) :
        while True:
                r = random.randint(1, 50)
                cx = random.randint(r, sample.width - r)
                cy = random.randint(r, sample.height - r)
                if not is_intersect(cx, cy, r, circles) :
                        break
        circles.append(CircleInfo(cx, cy, r))
        d.append(draw.Circle(cx, cy, r, fill='black', stroke_width=0, stroke='black'))

# Draw an arbitrary path (a triangle in this case)
# p = draw.Path(stroke_width=2, stroke='lime', fill='black', fill_opacity=0.2)
# p.M(-10, -20)  # Start path at point (-10, -20)
# p.C(30, 10, 30, -50, 70, -20)  # Draw a curve to (70, -20)
# d.append(p)

# # Draw text
# d.append(draw.Text('Basic text', 8, -10, -35, fill='blue'))  # 8pt text at (-10, -35)
# d.append(draw.Text('Path text', 8, path=p, text_anchor='start', line_height=1))
# d.append(draw.Text(['Multi-line', 'text'], 8, path=p, text_anchor='end', center=True))

# # Draw multiple circular arcs
# d.append(draw.ArcLine(60, 20, 20, 60, 270,
#         stroke='red', stroke_width=5, fill='red', fill_opacity=0.2))
# d.append(draw.Arc(60, 20, 20, 90, -60, cw=True,
#         stroke='green', stroke_width=3, fill='none'))
# d.append(draw.Arc(60, 20, 20, -60, 90, cw=False,
#         stroke='blue', stroke_width=1, fill='black', fill_opacity=0.3))

# # Draw arrows
# arrow = draw.Marker(-0.1, -0.51, 0.9, 0.5, scale=4, orient='auto')
# arrow.append(draw.Lines(-0.1, 0.5, -0.1, -0.5, 0.9, 0, fill='red', close=True))
# p = draw.Path(stroke='red', stroke_width=2, fill='none',
#         marker_end=arrow)  # Add an arrow to the end of a path
# p.M(20, 40).L(20, 27).L(0, 20)  # Chain multiple path commands
# d.append(p)
# d.append(draw.Line(30, 20, 0, 10,
#         stroke='red', stroke_width=2, fill='none',
#         marker_end=arrow))  # Add an arrow to the end of a line

d.set_pixel_scale(1)  # Set number of pixels per geometry unit
#d.set_render_size(400, 200)  # Alternative to set_pixel_scale
d.save_svg('example.svg')
d.save_png('example.png')
img = mpimg.imread('example.png')
imgplot = plt.imshow(img)
plt.show()
print(circles)