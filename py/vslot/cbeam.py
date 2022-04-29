from solid import *
from solid.utils import *  # Not required, but the utils module is useful
from vslot2020 import *

def make_cbeam(height):
    cbeam = make_2020(height);
    cbeam += right(20)(
        make_2020(height)
    );
    cbeam += forward(20)(
        make_2020(height)
    );
    cbeam += forward(40)(
        make_2020(height)
    );
    cbeam += forward(60)(
        make_2020(height)
    );
    cbeam += forward(60)(
        right(20)(
            make_2020(height)
        )
    );

    cbeam -= right(18.2)(
        forward(4.5)(
            cube([3.6, 11, height])
        )
    );

    cbeam -= right(4.5)(
        forward(18.2)(
            cube([11, 3.6, height])
        )
    );

    cbeam -= right(4.5)(
        forward(38.2)(
            cube([11, 3.6, height])
        )
    );

    cbeam -= right(4.5)(
        forward(58.2)(
            cube([11, 3.6, height])
        )
    );

    cbeam -= right(18.2)(
        forward(64.5)(
            cube([3.6, 11, height])
        )
    );

    return cbeam;


scad_render_to_file(make_cbeam(250), '../../scad/cbeam_250mm.scad');
scad_render_to_file(make_cbeam(500), '../../scad/cbeam_500mm.scad');
scad_render_to_file(make_cbeam(1000), '../../scad/cbeam_1000mm.scad');
scad_render_to_file(make_cbeam(1500), '../../scad/cbeam_1500mm.scad');
scad_render_to_file(make_cbeam(2000), '../../scad/cbeam_2000mm.scad');