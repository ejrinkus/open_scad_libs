from solid import *
from solid.utils import *  # Not required, but the utils module is useful
from vslot2020 import *

def center_hole_4040(height):
    points = [
        [15.2, 0.0, 0.0],
        [21.2, 0.0, 0.0],
        [21.2, 2.26, 0.0],
        [24.3, 5.36, 0.0],
        [24.3, 12.1, 0.0],
        [31.04, 12.1, 0.0],
        [34.14, 15.2, 0.0],
        [36.4, 15.2, 0.0],
        [36.4, 21.2, 0.0],
        [34.14, 21.2, 0.0],
        [31.04, 24.3, 0.0],
        [24.3, 24.3, 0.0],
        [24.3, 31.04, 0.0],
        [21.2, 34.14, 0.0],
        [21.2, 36.4, 0.0],
        [15.2, 36.4, 0.0],
        [15.2, 34.14, 0.0],
        [12.1, 31.04, 0.0],
        [12.1, 24.3, 0.0],
        [5.36, 24.3, 0.0],
        [2.26, 21.2, 0.0],
        [0.0, 21.2, 0.0],
        [0.0, 15.2, 0.0],
        [2.26, 15.2, 0.0],
        [5.36, 12.1, 0.0],
        [12.1, 12.1, 0.0],
        [12.1, 5.36, 0.0],
        [15.2, 2.26, 0.0],
        [15.2, 0.0, 0.0]
    ];

    solid = linear_extrude(height = height, center = False, convexity = 10, twist = 0)(
        polygon(points)
    );

    solid += right(8.2)(
        forward(8.2)(
            linear_extrude(height=height, center=False, convexity=10, twist=0)(
                arc_inverted(rad=3.9, start_degrees=0, end_degrees=90, segments=50)
            )
        )
    );

    solid += right(28.19)(
        forward(8.2)(
            linear_extrude(height=height, center=False, convexity=10, twist=0)(
                arc_inverted(rad=3.9, start_degrees=90, end_degrees=180, segments=50)
            )
        )
    );

    solid += right(28.19)(
        forward(28.19)(
            linear_extrude(height=height, center=False, convexity=10, twist=0)(
                arc_inverted(rad=3.9, start_degrees=180, end_degrees=270, segments=50)
            )
        )
    );

    solid += right(8.2)(
        forward(28.19)(
            linear_extrude(height=height, center=False, convexity=10, twist=0)(
                arc_inverted(rad=3.9, start_degrees=270, end_degrees=360, segments=50)
            )
        )
    );

    return solid;


def make_4040(height):
    extrusion = make_2020(height);
    extrusion += right(20)(
        make_2020(height)
    );
    extrusion += forward(20)(
        make_2020(height)
    );
    extrusion += forward(20)(
        right(20)(
            make_2020(height)
        )
    );

    extrusion -= forward(1.8)(
        right(1.8)(
            center_hole_4040(height)
        )
    );

    return extrusion;

# Render
scad_render_to_file(center_hole_4040(100), '../vslot4040hole.scad');
scad_render_to_file(make_4040(100), '../vslot4040.scad');