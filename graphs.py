from base import *
import random
HEIGHT = 200


# Base shapes

def circle_mark():
    big = circle(2).fill_color(papaya).line_width(0.1)
    small = circle(1.5).fill_color(white).line_width(0.1)
    return (big + small).scale_x(1)


def origin():
    return rectangle(1, 1).translate(0.5, -0.5).fill_color(white).line_color(white) + (vrule(1).translate(0, -0.5) + hrule(1).translate(0.5, 0)).line_width(0.05)

def d_mark():
    # big = Primitive.from_shape(Path.polygon(4, 2)).fill_color(papaya).line_width(0.1)
    # small = Primitive.from_shape(Path.polygon(4, 1).reverse()).line_width(0.1)
    return rectangle(1, 1).rotate_by(0.25/ 2).line_width(0.2).scale_uniform_to_x(0.1).fill_color(blue)

def x_mark():    
    big = rectangle(2, 1).fill_color(black).line_width(0)
    small = rectangle(1.25, 0.25).fill_color(Color("red")).line_width(0)
    def make_x(d):
        return d.rotate_by(0.25 / 2)  + d.rotate_by(-0.25 / 2) 
    return (make_x(big) + make_x(small)).scale_uniform_to_x(0.1)



def points(m, pts):
    return place_on_path([m] * len(pts),
                         Path.from_list_of_tuples(pts).reflect_y())



# Make picks

rpoints = [(random.random()*0.9  + 0.05, random.random() * 0.9 + 0.05) for _ in range(15)]

def linear(w, b):
    def model(x1, x2):
        return w[0] * x1 + w[1] * x2  + b
    return model

model1 = linear((1, 1), -1)

lin1 = linear((0.9, 1), -0.5)
lin2 = linear((-1, -0.9), 1.5)
def relu(x):
    return x if x > 0 else 0

def model2(x1, x2):
    return (relu(-lin1(x1, x2)) + relu(-lin2(x1, x2)))

def split(model):
    return \
        {"b" :  [points(x_mark(), [x]) for x in rpoints if model(*x) > 0],
         "r" :  [points(d_mark(), [x]) for x in rpoints if model(*x) <= 0]}

def draw_graph(f, c1=Color("red"), c2=Color("blue")):
    return origin() + quad(lambda x1, x2: f(x1, x2) > 0, Point(0.0, 0.0), 1, c1, c2).reflect_y()

model1_y = split(model1)
model2_y = split(model2)


# def image_pt2():
#     return make_path([(0, 0), (1, 1), (0, 0), (-1, 1), (0, 0), (1, -1), (0, 0)])

# def image_pt3():
#     return x_mark()

def image_split1():
    return make_path([(0, 0), (0, -1)]) + make_path([(0, 0), (1, 0)]) + circle_mark()


def image_data1():
    return origin() + model1_y["b"][0]

def image_data2():
    return origin() + model1_y["r"][0]

def image_data3():
    return origin() + model1_y["b"][0]

def image_data4():
    return origin() + concat(model1_y["r"])

def image_data5():
    return origin() + concat(model1_y["b"])

def image_correct():
    return draw_graph(model1) + concat(model1_y["b"] + model1_y["r"])


def image_incorrect():
    return draw_graph(linear((1, 1), -1.5)) + concat(model1_y["b"] + model1_y["r"])



# def image_incorrect():
#     return draw_graph(lambda x, y : 0.2 * x *  x * x - y + 0.5  > 0) + x_points + d_points


def image_bias():
    return draw_graph(linear((1, 1), -1)).center_xy() | hrule(1) | draw_graph(linear((1, 1), -0.75)).center_xy()

def image_wchange():
    return draw_graph(linear((1, 1), -1)).center_xy() | hrule(1) | draw_graph(linear((1, 1.5), -1)).center_xy()


def image_model():
    return [draw_graph(linear((1, 1), -1.4)),
            draw_graph(model2),
            draw_graph(model2)
            ]


def image_mlpgraph():
    return draw_graph(model2) +  concat(model2_y["b"] + model2_y["r"])


def image_split():
    return concat(model2_y["b"] + model2_y["r"])

def image_splitfail():
    return draw_graph(model1) + concat(model2_y["b"] + model2_y["r"])

def image_split1():
    return draw_graph(lin2, Color("white"), Color("yellow")) + concat(model2_y["b"] + model2_y["r"])

def image_split2():
    return draw_graph(lin1, Color("white"), Color("green")) + concat(model2_y["b"] + model2_y["r"])



def image_mlp():
    return draw_graph(model1)
# lambda x, y : (0.9 * x + y - 0.5  > 0) and (x + 0.9* y - 1.5  < 0) ).center_xy() 



def image_sigmoid():
    return function(lambda x : 1 / (1 + math.exp(-x)), -10, 10)



def image_relu():
    r = lambda x : 0 if x < 0 else x
    return function(r, -1, 1).line_width(0.01) + points(x_mark(), [(p[0], r(p[0])) for p in x]) + points(d_mark(), [(p[0], r(p[0])) for p in d])

if __name__ == "__main__":
    render(locals(), "Graphs", HEIGHT)
