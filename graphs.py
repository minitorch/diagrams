from base import *
HEIGHT = 200

def circle_mark():
    big = circle(2).fill_color(papaya).line_width(0.1)
    small = circle(1.5).fill_color(white).line_width(0.1)
    return big + small

def x_mark():    
    big = rectangle(2, 1).fill_color(black).line_width(0)
    small = rectangle(1.5, 0.5).fill_color(Color("red")).line_width(0)
    def make_x(d):
        return d.rotate_by(0.25 / 2)  + d.rotate_by(-0.25 / 2) 
    return make_x(big) + make_x(small)


def image_pt2():
    return make_path([(0, 0), (1, 1), (0, 0), (-1, 1), (0, 0), (1, -1), (0, 0)])

def image_pt3():
    return x_mark()

def image_split1():
    return circle_mark()
    return make_path([(0, 0), (0, -1)]) + make_path([(0, 0), (1, 0)]) + circle_mark()



if __name__ == "__main__":
    render(locals(), "Graphs", HEIGHT)
