from ..grading import *
import numpy as np
from numpy.testing import assert_equal, assert_allclose
from scipy.integrate import quad
from functools import partial


def test_total_mark_xc():
    """testing first function
    """
    np.testing.assert_almost_equal(total_mark_xc([100, 100, 100, 100], 0), 80)
    np.testing.assert_almost_equal(total_mark_xc([0, 0], 100, 0), 100)
    np.testing.assert_almost_equal(total_mark_xc([0, 0], 0, 1200), 40)
    np.testing.assert_almost_equal(total_mark_xc([0, 0], 0, 2400), 40)
    assignments = [100, 100, 100, 30, 90, 50, 100, 0, 75, 80]
    np.testing.assert_almost_equal(total_mark_xc(assignments, 70, 500), 85.333333333333333)
    assignments = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    np.testing.assert_almost_equal(total_mark_xc(assignments, 50, 700), 70.03030303030303)

def test_total_mark_xc_mult():
    """
    testing second function
    """
    assignments = np.array(
        [
            [100, 100, 100, 100],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 40, 70, 100],
        ]
    )
    exam = np.array([0, 100, 0, 0, 50])
    extra_credit_pages = np.array([0, 0, 1200, 1800, 700])
    np.testing.assert_almost_equal(
        total_mark_xc_mult(assignments, exam, extra_credit_pages),
        [80.0, 100.0, 40.0, 40.0, 72.4],
    )
