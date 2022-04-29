// Generated by SolidPython 1.1.3 on 2022-04-28 23:56:22


difference() {
	cube(size = [20.0000000000, 20.0000000000, 500]);
	translate(v = [5.1000000000, 0, 0]) {
		linear_extrude(center = false, convexity = 10, height = 500, twist = 0) {
			polygon(points = [[0.0000000000, 0.0000000000], [1.8000000000, 1.8000000000], [-0.6000000000, 1.8000000000], [-0.6000000000, 3.4400000000], [2.0600000000, 6.1000000000], [7.7400000000, 6.1000000000], [10.4000000000, 3.4400000000], [10.4000000000, 1.8000000000], [8, 1.8000000000], [9.8000000000, 0.0000000000], [0.0000000000, 0.0000000000]]);
		}
	}
	translate(v = [0, 14.9000000000, 0]) {
		rotate(a = [0, 0, 270]) {
			linear_extrude(center = false, convexity = 10, height = 500, twist = 0) {
				polygon(points = [[0.0000000000, 0.0000000000], [1.8000000000, 1.8000000000], [-0.6000000000, 1.8000000000], [-0.6000000000, 3.4400000000], [2.0600000000, 6.1000000000], [7.7400000000, 6.1000000000], [10.4000000000, 3.4400000000], [10.4000000000, 1.8000000000], [8, 1.8000000000], [9.8000000000, 0.0000000000], [0.0000000000, 0.0000000000]]);
			}
		}
	}
	translate(v = [14.9000000000, 0, 0]) {
		translate(v = [0, 20.0000000000, 0]) {
			rotate(a = [0, 0, 180]) {
				linear_extrude(center = false, convexity = 10, height = 500, twist = 0) {
					polygon(points = [[0.0000000000, 0.0000000000], [1.8000000000, 1.8000000000], [-0.6000000000, 1.8000000000], [-0.6000000000, 3.4400000000], [2.0600000000, 6.1000000000], [7.7400000000, 6.1000000000], [10.4000000000, 3.4400000000], [10.4000000000, 1.8000000000], [8, 1.8000000000], [9.8000000000, 0.0000000000], [0.0000000000, 0.0000000000]]);
				}
			}
		}
	}
	translate(v = [20.0000000000, 0, 0]) {
		translate(v = [0, 5.1000000000, 0]) {
			rotate(a = [0, 0, 90]) {
				linear_extrude(center = false, convexity = 10, height = 500, twist = 0) {
					polygon(points = [[0.0000000000, 0.0000000000], [1.8000000000, 1.8000000000], [-0.6000000000, 1.8000000000], [-0.6000000000, 3.4400000000], [2.0600000000, 6.1000000000], [7.7400000000, 6.1000000000], [10.4000000000, 3.4400000000], [10.4000000000, 1.8000000000], [8, 1.8000000000], [9.8000000000, 0.0000000000], [0.0000000000, 0.0000000000]]);
				}
			}
		}
	}
	translate(v = [0, 10.0000000000, 0]) {
		translate(v = [10.0000000000, 0, 0]) {
			cylinder($fn = 50, h = 500, r = 2.1000000000);
		}
	}
}
/***********************************************
*********      SolidPython code:      **********
************************************************
 
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
 
************************************************/
