from base import *

HEIGHT = 200

# Style 
def ta(text):
    return t(text, 0.3)

def tensor(skew, depth, rows, columns, name=""):
    s = Vector(0, 0)
    up = Vector(0, -1)
    right = Vector(1, 0)
    hyp = Vector(skew, -math.sqrt(1 - skew))
    def quad(v1, v2):
        return Trail([s, v1, v2, -v1, -v2]).stroke()
    # Faces
    face_t, face_r, face_m = quad(-hyp, right), quad(up, hyp), quad(-up, right) 

    # Make a single cube with bounding box around the front face
    cube = (face_m + face_t.align_l().align_b()).align_t().align_r() + face_r.align_t().align_r()
    return concat(([cube.translate_by(hyp * i + -up * j + right * k).named((name, i, j, k))
                    for i in reversed(range(depth))
                    for j in reversed(range(rows))
                    for k in range(columns)]))


def image_matrix1():
    return t("matrix", 1) / v /  matrix("m", 2, 5).center_xy()

def image_matrix1():
    return matrix("m", 2, 5)

def image_matrix2():
     return matrix("m", 5, 2)

# Strid1
def image_stride1():
    m = matrix("x", 5, 2)
    s = matrix("s", 1, 10).fill_color(papaya)
    base = t("tensor") / v / m / v / s / t("storage")

    d = base + connect_all(base, [(("x", 0, 0), ("s", 0, 0)),
                                  (("x", 0, 1), ("s", 0, 1)),
                                  (("x", 1, 0 ), ("s", 0, 2)),
                                  (("x", 4, 1 ), ("s", 0, 9))]).dashing([0.1, 0.1], 0).line_width(0.1)
    




    d2 = base + connect_all(base, [(("x", 0, 0), ("s", 0, 0)),
                                  (("x", 1, 0), ("s", 0, 1)),
                                  (("x", 0, 1), ("s", 0, 2)),
                                  (("x", 4, 1), ("s", 0, 9))]).dashing([0.1, 0.1], 0).line_width(0.1)
    
    return [d1, d2]




m = (tensor(0.5, 1, 3, 2).align_l().align_b().line_width(0) + matrix("a", 3, 2).align_l().align_b()).align_b() | h |  tensor(0.5, 2, 1, 2).align_b() | h |  (tensor(0.5, 2, 3, 2).align_l().align_b().line_color(papaya) + matrix("", 3, 2).align_l().align_b()).align_b() | h | (tensor(0.5, 2, 3, 2).align_l().align_b().line_color(papaya).align_t().align_l() + tensor(0.5, 2, 1, 2).align_t().align_l() ).align_b()  | h | tensor(0.5, 2, 3, 2).align_l().align_b()
m.line_width(0.02).render_svg(pathsvg, HEIGHT)




up = Vector(0, 1)


exit()
d = make_path([(0, 0), (-skew, 1.), (1 - skew, 1.), (1, 0), (0, 0)]).fill_opacity(0).line_width(0.05)

d =  d.pad_l(-skew).show_bounding_box()
# d = h | d | d | d | h


d =  (tile(d, 3, 1, "x").reflect_x().reflect_y() / tile(d, 3, 1, "x"))#.translate(1, 0.75)  
d = d / (matrix("", 3, 3) | d.rotate_by(0.25).reflect_y().translate(0, -0.75)) 
pathsvg = "diagrams/Tensors/test.svg"
d.render_svg(pathsvg, HEIGHT)


down = Vector(0, -10)
upright = Vector(7, 5) 
right = Vector(15, 0)


point = circle(0.2).line_width(0.5)

d = concat([point,
            point.translate_by(right),
            point.translate_by(upright),
            point.translate_by(down),
            point.translate_by(right + down),
            point.translate_by(down + upright),
            point.translate_by(upright + right),
            point.translate_by(down + right + upright)
])

# d.render_svg(pathsvg, HEIGHT)
