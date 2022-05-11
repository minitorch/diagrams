from base import *

HEIGHT = 200

right_arrow = make_path([(0, 0), (1, 0)], True).line_width(0.03).center_xy()
left_arrow = make_path([(1, 0), (0, 0)], True).line_width(0.03).center_xy()
box = rectangle(1.5, 1).line_width(0.05).fill_color(grey)
bbox = rectangle(1.5, 1).line_width(0.05).fill_color(papaya)
def ta(text):
    return t(text, 0.3)


d = right_arrow.named("in") | box | right_arrow.named("out")
d += label_above(d, "in", ta("x"))
d += label_above(d, "out", ta("f(x)"))

d.render_svg("diagrams/Autograd/autograd1.svg", HEIGHT)


d = (right_arrow.named("x") / vstrut(0.8) / right_arrow.named("y")).center_xy() | box | right_arrow.named("out")
d += label_above(d, "x", ta("x"))
d += label_below(d, "y", ta("y"))
d += label_above(d, "out", ta("f(x, y)"))

d.render_svg("diagrams/Autograd/autograd2.svg", HEIGHT)

d = left_arrow.named("out") | bbox | left_arrow.named("in")
d += label_above(d, "out", ta("f'(x)"))
d += label_above(d, "in", ta("d_out"))

d.render_svg("diagrams/Autograd/autograd3.svg", HEIGHT)

d = (left_arrow.named("x") / vstrut(0.8) / left_arrow.named("y")).center_xy() | bbox | left_arrow.named("out")
d += label_above(d, "x", ta("f_x'(x, y)"))
d += label_below(d, "y", ta("f_y'(x, y)"))
d += label_above(d, "out", ta("d_out"))

d.render_svg("diagrams/Autograd/autograd4.svg", HEIGHT)



d = (right_arrow / vstrut(0.8) / right_arrow).center_xy() | box.named("l") | hstrut(1) | (box.named("t") / vstrut(1) / box.named("b")).center_xy() | hstrut(1) | box.named("r") | right_arrow 

d += connect_outer(d, "l", "E", "t", "W").line_width(0.03)
d += connect_outer(d, "l", "E", "b", "W").line_width(0.03)
d += connect_outer(d, "t", "E", "r", "W").line_width(0.03)
d += connect_outer(d, "b", "E", "r", "W").line_width(0.03)

d.render_svg("diagrams/Autograd/autograd5.svg", HEIGHT)


d = right_arrow.named("in") | box | right_arrow.named("out") | box | right_arrow.named("out2")
d += label_above(d, "in", ta("x"))
d += label_above(d, "out", ta("g(x)"))
d += label_above(d, "out2", ta("f(g(x))"))

d.render_svg("diagrams/Autograd/chain1.svg", HEIGHT)
