from colour import Color
from chalk import *
from chalk.bounding_box import BoundingBox

# Library 

# Colors
papaya = Color("#ff9700")
blue = Color("#005FDB")
olive = Color("#708238")
black = Color("#000000")
white = Color("#ffffff")
grey = Color("#bbbbbb")

# Text
def t(te, s=1):
    return text(te, s).fill_color(black).line_color(white)


# Tiling 
def tile(d, m, n, name = ""):
    return hcat(vcat(d.named((name, j, i)) for j in range(n)) for i in range(m)).center_xy()


def connect_all(d, names):
    return concat([
        connect(d, a, b)
        for a, b in names])
    

# Define spacing

def hstrut(width=0.2): return hrule(width).line_width(0)
def vstrut(height=0.5): return vrule(height).line_width(0)

v = vstrut(2.5)
v2 = vstrut(1.25)
h = hstrut(2.5)

def pad(d, x):
    return d.pad_l(x).pad_r(x).pad_t(x).pad_b(x)


# Arrows

# Arrow Labels
def label(t):
    return circle(0.5).fill_color(white).line_color(white) + text(t, 0.5).fill_color(black)


# Label above

def label_above(d, name, label):
    b = d.get_subdiagram_bounding_box(name)
    return label.translate(b.center.x, b.top - label.get_bounding_box().height)

def label_below(d, name, label):
    b = d.get_subdiagram_bounding_box(name)
    return label.translate(b.center.x, b.bottom + label.get_bounding_box().height)


def surround(diagram):
    bb = diagram.get_bounding_box()
    rect = rectangle(bb.width + 2, bb.height + 2, 1.0)
    return rect + diagram.center_xy()

def cover(d, a, b):
    b1 = d.get_subdiagram_bounding_box(a)
    b2 = d.get_subdiagram_bounding_box(b)
    new_bb = BoundingBox(b1.tl, b2.br)
    return rectangle(new_bb.width, new_bb.height, 0.0) \
            .translate(new_bb.center.x, new_bb.center.y)


# Matrix

def cell():
    return rectangle(1, 1).line_width(0.05)

def matrix(n, r, c):
    return tile(cell(), c, r, n)

