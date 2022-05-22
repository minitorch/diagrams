from base import *


HEIGHT = 200


mark = circle(0.1).line_width(0.05).fill_color(papaya)

def f(x):
    return x * x + 0.5

def image_tangent():
    return function(f).show_bounding_box()


def image_function():
    return concat([function(f),
                   function(lambda x: 0.0),
                   make_path([(0.5, 0.0), (0.5, -f(0.5))]).line_width(0.05).dashing([0.1, 0.1], 0.0),
                   mark.translate(0.5, -f(0.5)),
    ])


def image_approx():
    return concat([function(f, l=0, r = 0.9),
                   function(lambda x: x, -0.5, 0.5).line_color(Color("red")).translate(0.5, -f(0.5)).dashing([0.01, 0.05], 0.0),
                   (circle(0.05).line_width(0.05) / vstrut(0.2) / t("f'" , 0.3)).translate(0.5, -f(0.5)).fill_color(Color("red")) ,
                   (circle(0.05).line_width(0.05)).translate(0.3, -f(0.3)).fill_color(papaya),
                   (t("f" , 0.3) // vstrut(0.2) // circle(0.05).line_width(0.05)).translate(0.7, -f(0.7)).fill_color(papaya),
                   
    ])


if __name__ == "__main__":
    render(locals(), "Grad", HEIGHT)
