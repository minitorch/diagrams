from base import *

HEIGHT = 200



right_arrow = make_path([(0, 0), (1, 0)], True).line_width(0.03).center_xy()
right_arrow = right_arrow.pad_r(0.4).pad_l(0.4)

m3_2 = matrix("a", 3, 2)
m1_1 = matrix("b", 1, 1)
m3_1 = matrix("c", 3, 1)

def lb(te, d):
    return d / t(te, 0.5).pad_b(0.4)


def image_scalar():
    def col(c):
        return (m3_2.line_color(c).align_t().align_l() + m1_1.align_t().align_l()).center_xy()

    return hcat([lb("(3, 2)", m3_2), col(white),
                 right_arrow, m3_2, col(papaya),
                 right_arrow, m3_2], 0.4)

def image_vector():
    def col(c):
        return (m3_2.line_color(c).align_t().align_l() + m3_1.align_t().align_l()).center_xy()
    return hcat([lb("(3, 2)", m3_2),
                 lb("(3, 1)", col(white)),
                 right_arrow,
                 m3_2, col(papaya), right_arrow, m3_2], 0.4)


def tensor(depth, rows, columns):
    "Draw a tensor"
    
    up = Vector(0, -1)
    right = Vector(1, 0)
    hyp = (up * 0.5).shear_x(-1)
    
    # Faces
    face_m = rectangle(1, 1).align_tl().show_origin()
    face_t = rectangle(1, 0.5).shear_x(-1).align_bl()
    face_r = rectangle(0.5, 1).shear_y(-1).align_tr()
    

    # Make a single cube with bounding box around the front face
    cube = (face_m + face_t).align_tr() + face_r
    return concat(([cube.translate_by(hyp * i + -up * j + right * k)
                    for i in reversed(range(depth))
                    for j in reversed(range(rows))
                    for k in range(columns)]))


def image_threed():
    def t(d, r, c):
        return tensor(d, r, c).fill_color(white)



    d, r, c = 3, 4, 5

    base = t(d, r, c).line_color(papaya)
    return hcat([t(1, r, c),  t(d, 1, c), label("→"), (base + t(1, r, c)), (base + t(d, 1, c) ), label("="), t(d, r, c)], sep=2.5)

    

HEIGHT = 200

if __name__ == "__main__":
    render(locals(), "Broadcast", HEIGHT)
