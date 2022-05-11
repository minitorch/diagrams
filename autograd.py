from base import *

HEIGHT = 200


# General tools

right_arrow = make_path([(0, 0), (1, 0)], True).line_width(0.03).center_xy()
left_arrow = right_arrow.reflect_x()
upr_arrow = make_path([(0, 0), (1, -0.5)], True).line_width(0.03).center_xy()
downr_arrow = upr_arrow.reflect_y()
box = rectangle(1.5, 1).line_width(0.05).fill_color(grey).pad_b(0.5).pad_t(0.5).pad_l(0.1).pad_r(0.1).center_xy()
bbox = rectangle(1.5, 1).line_width(0.05).fill_color(papaya).pad_b(0.5).pad_t(0.5).pad_l(0.1).pad_r(0.1).center_xy()
def ta(text):
    return t(text, 0.3)
def label(text):
    return ta(text).pad_b(0.2).pad_t(0.2)
def arrow(text, btext="", d=True):
    return (label(text) // (right_arrow if d else left_arrow) / label(btext))

def arrow(text, btext="", d=True):
    return (label(text) // (right_arrow if d else left_arrow) / label(btext))

def r(x):
    return x.reflect_x().reflect_y()

# Autograd 1
d = arrow("x") | box | arrow("f(x)")
d.render_svg("diagrams/Autograd/autograd1.svg", HEIGHT)


# Autograd 2
d = (arrow("x")  / arrow("", "y")).center_xy() | box | arrow("out")
d.render_svg("diagrams/Autograd/autograd2.svg", HEIGHT)


# Autograd 3
d = arrow("f'(x)", "", False) | bbox | arrow("d_out", "", False)
d.render_svg("diagrams/Autograd/autograd3.svg", HEIGHT)

d = (arrow("f_x'(x, y)", "", False) / arrow("", "f_y'(x, y)", False)).center_xy() | bbox | arrow("d_out", "", False)
d.render_svg("diagrams/Autograd/autograd4.svg", HEIGHT)



d = (arrow("") / arrow("")).center_xy() | box | ((upr_arrow | box | downr_arrow) / (downr_arrow | box | upr_arrow) ).center_xy()  | box | right_arrow 
d.render_svg("diagrams/Autograd/autograd5.svg", HEIGHT)


d = arrow("x", "") | box | arrow("g(x)", "") | box | arrow("f(g(x))", "")
d.render_svg("diagrams/Autograd/chain1.svg", HEIGHT)



def backprop(i):
    def c(d, j):
        return d.line_color(papaya) if i > j else d

    d = r(c(arrow(""), 6) / c(arrow(""), 5)).center_xy() | box | ((c(r(upr_arrow), 4) | box | c(r(downr_arrow), 3)) / (c(r(downr_arrow), 2) | box | c(r(upr_arrow), 1) )).center_xy()  | box | c(r(right_arrow), 0)
    d.render_svg(f"diagrams/Autograd/backprop{i}.svg", HEIGHT)

for i in range(1, 8):
    backprop(i)


