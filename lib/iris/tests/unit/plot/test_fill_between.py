# Copyright Iris contributors
#
# This file is part of Iris and is released under the BSD license.
# See LICENSE in the root of the repository for full licensing details.
"""Unit tests for the `iris.plot.fill_between` function."""

import numpy as np
import pytest

from iris.coords import DimCoord
from iris.cube import Cube
from iris.tests import _shared_utils

if _shared_utils.MPL_AVAILABLE:
    import iris.plot as iplt


@_shared_utils.skip_plot
class TestArgumentTypes(_shared_utils.GraphicsTest):
    @pytest.mark.parametrize(("position", "name"), [(0, "x"), (1, "y1"), (2, "y2")])
    def test_not_cube_or_coord(self, position, name):
        x = DimCoord([0.0, 1.0, 2.0], long_name="x")
        y1 = Cube([1.0, 2.0, 3.0], long_name="y1")
        y1.add_dim_coord(x, 0)
        args = [x, y1, y1.copy()]
        args[position] = np.arange(3)
        with pytest.raises(TypeError, match=f"{name} must be a cube or a coordinate"):
            iplt.fill_between(*args)
