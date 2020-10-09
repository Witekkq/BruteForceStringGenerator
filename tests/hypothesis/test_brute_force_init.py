from hypothesis import given, strategies as st
from string_generator.brute_force_string_generator import BruteForceStringGenerator


@given(st.text(min_size=0))
def test_decodes_to_starting_sequence(ls):
    obj = BruteForceStringGenerator(sequence=ls)
    assert obj.__repr__() == ls
