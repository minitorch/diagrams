from base import *

robot = rectangle(1, 1).line_color(grey).fill_color(grey) + image("diagrams/gpu/robot.png", "robot.png").scale_uniform_to_x(1).pad_b(-0.15).pad_t(-0.15).pad_l(-0.15).pad_r(-0.15).scale_uniform_to_x(1)

def image_thread():
    return robot

def image_block1d():
    return vcat([t("block", 0.5), tile(robot, 8, 1)], 0.4)

def nblock(n):
    return tile(robot, 4, 3, n)
block = nblock("b")
def image_block():
    return vcat([t("block", 0.5), block], 0.4)

def image_blockid():
    d = tile(block.pad_r(0.5).pad_b(0.5).pad_l(0.5).pad_t(0.5), 3, 3, "n")
    d = cover(d, ("n", 1, 1), ("n", 1, 1)) + d
    return vcat([t("grid", 1.0),
                 (t("blockidx.y", 0.5).rotate_by(0.25) | t("blockidx.x", 0.5) // d).center_xy()], 0.5)


def image_sharedmem():
    d =  hcat([block,
              rectangle(1.5, 1).line_color(papaya).line_width(0.2).named("mem")], 0.5)
    d += connect(d, ("b", 0, 2), "mem").line_color(papaya).line_width(0.1)
    d += connect(d, ("b", 2, 1), "mem").line_color(papaya).line_width(0.1)
    return vcat([t("block shared memory",0.3), d], 0.5)

def image_map():
    d = vcat([nblock(i) for i in range(3)], 0.5).center_xy()
    d = hcat([d, matrix("m", 7, 3).scale(1.5)], 0.5)
    d += cover(d, (0, 0, 3),  (0, 2, 3)).fill_color(black)
    d += cover(d, (1, 0, 3),  (1, 2, 3)).fill_color(black)
    d += cover(d, (2, 0, 3),  (2, 2, 3)).fill_color(black)
    d += cover(d, (2, 1, 0),  (2, 2, 3)).fill_color(black)

    d += connect(d, (0, 1, 1),  ("m", 1, 1)).line_color(papaya).line_width(0.2)
    return d

HEIGHT = 200

if __name__ == "__main__":
    render(locals(), "gpu", HEIGHT)
