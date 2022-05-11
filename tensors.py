from base import *

def ta(text):
    return t(text, 0.3)


def cell():
    return rectangle(1, 1).line_width(0.05)
def matrix(n, r, c):
    return tile(cell(), c, r, n)


d = t("matrix", 1) / v /  matrix("m", 2, 5).center_xy()
d.render_svg("diagrams/Tensors/matrix.svg", 40)

d = matrix("m", 2, 5)
d.render_svg("diagrams/Tensors/matrix1.svg", 40)

d = matrix("m", 5, 2)
d.render_svg("diagrams/Tensors/matrix2.svg", 40)


# 


m = matrix("x", 5, 2)
s = matrix("s", 1, 10).fill_color(papaya)
base = t("tensor") / v / m / v / s / t("storage")

# 
d = base + (concat([connect(base, ("x", 0, 0), ("s", 0, 0)),
                    connect(base, ("x", 0, 1), ("s", 0, 1)),
                    connect(base, ("x", 1, 0 ), ("s", 0, 2)),
                    connect(base, ("x", 4, 1 ), ("s", 0, 9)),
])).dashing([0.1, 0.1], 0).line_width(0.1)

pathsvg = "diagrams/Tensors/stride1.svg"
d.render_svg(pathsvg, 200)

d = base + (concat([connect(base, ("x", 0, 0), ("s", 0, 0)),
                    connect(base, ("x", 1, 0), ("s", 0, 1)),
                    connect(base, ("x", 0, 1), ("s", 0, 2)),
                    connect(base, ("x", 4, 1), ("s", 0, 9)),
])).dashing([0.1, 0.1], 0).line_width(0.1)

pathsvg = "diagrams/Tensors/stride2.svg"
d.render_svg(pathsvg, 200)
