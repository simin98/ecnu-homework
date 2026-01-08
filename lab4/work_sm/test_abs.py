from hypothesis import given
from hypothesis import strategies as st
from .abs_wrong import my_abs

@given(st.integers())
def test_abs_non_negative(x):
    result = my_abs(x)
    assert result >= 0
