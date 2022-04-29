from solid import *
from solid.utils import *  # Not required, but the utils module is useful

GROOVE_WIDTH = 9.8

def make_groove(height):
    # Define the shape of the vslot grooves as a polygon.
    groove_points = [
        [0.0, 0.0, 0.0],
        [1.8, 1.8, 0.0],
        [-0.6, 1.8, 0.0],
        [-0.6, 3.44, 0.0],
        [2.06, 6.1, 0.0],
        [7.74, 6.1, 0.0],
        [10.4, 3.44, 0.0],
        [10.4, 1.8, 0.0],
        [8, 1.8, 0.0],
        [9.8, 0.0, 0.0],
        [0.0, 0.0, 0.0],
    ];

    # Extrude the groove polygon into a 3d object.
    return linear_extrude(height = height, center = False, convexity = 10, twist = 0)(
        polygon(groove_points)
    );

def make_2020(height):
    # Overall dimensions
    side = 20.0;

    translate_dist = (side/2) - (GROOVE_WIDTH/2);

    bottom_groove = right(translate_dist)(
        make_groove(height)
    );

    left_groove = forward(translate_dist + GROOVE_WIDTH)(
        rotate([0, 0, 270])(
            make_groove(height)
        )
    );

    top_groove = right(translate_dist + GROOVE_WIDTH)(
        forward(side)(
            rotate([0, 0, 180])(
                make_groove(height)
            )
        )
    );
    
    right_groove = right(side)(
        forward(translate_dist)(
            rotate([0, 0, 90])(
                make_groove(height)
            )
        )
    );

    center_hole = forward(side/2)(
        right(side/2)(
            cylinder(h=height, r=2.1, segments=50)
        )
    );

    return cube([side, side, height]) - bottom_groove - left_groove - top_groove - right_groove - center_hole;

# Test renders
scad_render_to_file(make_2020(250), '../../scad/vslot2020_250mm.scad');
scad_render_to_file(make_2020(500), '../../scad/vslot2020_500mm.scad');
scad_render_to_file(make_2020(1000), '../../scad/vslot2020_1000mm.scad');
scad_render_to_file(make_2020(1500), '../../scad/vslot2020_1500mm.scad');
scad_render_to_file(make_2020(2000), '../../scad/vslot2020_2000mm.scad');
scad_render_to_file(make_groove(250), '../../scad/vslotgroove.scad');