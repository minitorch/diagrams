from base import *

HEIGHT = 200

# Style 
def ta(text):
    return t(text, 0.3)

def cell():
    return rectangle(1, 1).line_width(0.05)

def matrix(n, r, c):
    return tile(cell(), c, r, n)


d = t("matrix", 1) / v /  matrix("m", 2, 5).center_xy()
d.render_svg("diagrams/Tensors/matrix.svg", HEIGHT)

d = matrix("m", 2, 5)
d.render_svg("diagrams/Tensors/matrix1.svg", HEIGHT)

d = matrix("m", 5, 2)
d.render_svg("diagrams/Tensors/matrix2.svg", HEIGHT)

# Strid1
m = matrix("x", 5, 2)
s = matrix("s", 1, 10).fill_color(papaya)
base = t("tensor") / v / m / v / s / t("storage")
 
d = base + connect_all([(("x", 0, 0), ("s", 0, 0)),
                        (("x", 0, 1), ("s", 0, 1)),
                        (("x", 1, 0 ), ("s", 0, 2)),
                        (("x", 4, 1 ), ("s", 0, 9))]).dashing([0.1, 0.1], 0).line_width(0.1)

d.render_svg("diagrams/Tensors/stride1.svg", HEIGHT)



d = base + connect_all([(("x", 0, 0), ("s", 0, 0)),
                        (("x", 1, 0), ("s", 0, 1)),
                        (("x", 0, 1), ("s", 0, 2)),
                        (("x", 4, 1), ("s", 0, 9))]).dashing([0.1, 0.1], 0).line_width(0.1)

pathsvg = "diagrams/Tensors/stride2.svg"
d.render_svg(pathsvg, HEIGHT)
