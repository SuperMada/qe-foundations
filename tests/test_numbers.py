"""Tests for celsius_to_fahrenheit and letter_grade (function-style tests)."""
import pytest
import sys

from qe_utils import celsius_to_fahrenheit, letter_grade


# ---- WORKED EXAMPLE ----
@pytest.mark.smoke
def test_freezing_point_converts_to_32f():
    assert celsius_to_fahrenheit(0) == 32


# ---- TODO tests ----
@pytest.mark.regression
def test_boiling_point_converts_to_212f():

    assert celsius_to_fahrenheit(100) == 212

@pytest.mark.regression
def test_body_temperature_uses_approx():

    assert celsius_to_fahrenheit(37) == pytest.approx(98.6)

@pytest.mark.boundary
def test_minus_40_is_same_in_both_scales():

    assert celsius_to_fahrenheit(-40) == -40

@pytest.mark.boundary
@pytest.mark.smoke
def test_grade_90_is_a():

    assert letter_grade(90) == "A"

@pytest.mark.boundary
def test_grade_89_is_b():

    assert letter_grade(89) == "B"

@pytest.mark.boundary
def test_grade_0_is_f_and_100_is_a():
    # TODO (Task 3): the two extreme valid scores. Marker: boundary
    assert letter_grade(100) == "A"
    assert letter_grade(0) == "F"

@pytest.mark.regression
def test_grade_below_zero_raises_value_error():

    with pytest.raises(ValueError, match="score must be between 0 and 100"):
        letter_grade(-1)

@pytest.mark.regression
def test_grade_above_100_raises_value_error():

    with pytest.raises(ValueError, match="score must be between 0 and 100"):
        letter_grade(101)


# TODO (Task 5): add ONE test that uses @pytest.mark.skipif on a condition, e.g.
#   @pytest.mark.skipif(sys.version_info < (3, 8), reason="needs Python 3.8+")
# (import sys at the top). Any simple, truthful test is fine. Name it test_..._skipif_example.
@pytest.mark.skipif(sys.version_info < (3, 8), reason="needs Python 3.8+")
def test_grade_79_is_c_skipif_example():
    assert letter_grade(79) == "C"