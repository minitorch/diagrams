from base import *


# General tools

right_arrow = make_path([(0, 0), (1, 0)], True).line_width(0.03).center_xy()
left_arrow = right_arrow.reflect_x()
upr_arrow = make_path([(0, 0), (1, -0.5)], True).line_width(0.03).center_xy()
downr_arrow = upr_arrow.reflect_y()
box = rectangle(1.5, 1).line_width(0.05).pad_b(0.5).pad_t(0.5).center_xy().fill_color(grey)
bbox = box.fill_color(papaya)

def ta(text):
    return t(text, 0.3)
def label(text):
    return ta(text).pad_b(0.2).pad_t(0.2)
def arrow(text, btext="", d=True):
    return (label(text) // (right_arrow if d else left_arrow) / label(btext))

def r(x):
    return x.reflect_x().reflect_y()


def image_autograd1():
    return hcat([arrow("x"), box, arrow("f(x)")], 0.1)

def image_autograd2():
    return hcat([(arrow("x")  / arrow("", "y")).center_xy(), box, arrow("out")], 0.1)

def image_autograd3():
    return hcat([arrow("f'(x)", "", False), bbox, arrow("d_out", "", False)], 0.1)

def image_autograd4():
    return hcat([(arrow("f_x'(x, y)", "", False) / arrow("", "f_y'(x, y)", False)).center_xy(),  bbox, arrow("d_out", "", False)], 0.1)

def image_autograd5():
    return hcat([(arrow("") / arrow("")).center_xy(), box, ((upr_arrow | box | downr_arrow) / (downr_arrow | box | upr_arrow) ).center_xy(), box, right_arrow], 0.1)


def image_chain1():
    return hcat([arrow("x"), box, arrow("g(x)"), box, arrow("f(g(x))")], 0.1)


def image_backprop():
    def backprop(i):
        def c(d, j):
            return d.line_color(papaya) if i > j else d

        return hcat([r(c(arrow(""), 6) / c(arrow(""), 5)).center_xy(),
                     box,
                     ((c(r(upr_arrow), 4) | box | c(r(downr_arrow), 3)) / (c(r(downr_arrow), 2) |  box |bn c(r(upr_arrow), 1))).center_xy(),
                     box,
                     c(r(right_arrow), 0)], 0.1)

    return [backprop(i) for i in range(1, 8)]

HEIGHT = 200

if __name__ == "__main__":
    render(locals(), "Autograd", HEIGHT)
