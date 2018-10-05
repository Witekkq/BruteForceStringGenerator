import string
import pytest

from brute_force_string_generator import BruteForceStringGenerator, Direction


def test_brute_force_empty():
    default_init = BruteForceStringGenerator()
    assert (default_init.next_string() == 'a')


def test_brute_force_direction():
    direction_test = BruteForceStringGenerator(sequence='aa', dir=Direction.LEFT)
    assert (direction_test.next_string() == 'ba')
    direction_test = BruteForceStringGenerator(sequence='aa', dir=Direction.RIGHT)
    assert (direction_test.next_string() == 'ab')


def test_brute_force_edge():
    direction_test = BruteForceStringGenerator(sequence='za', dir=Direction.LEFT)
    assert (direction_test.next_string() == 'ab')
    direction_test = BruteForceStringGenerator(sequence='az', dir=Direction.RIGHT)
    assert (direction_test.next_string() == 'ba')


def test_brute_force_long_string():
    long_string = BruteForceStringGenerator(sequence='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    assert (long_string.next_string() == 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab')


def test_brute_force_for_loop():
    loop_string = BruteForceStringGenerator(min_length=3)
    for _ in range(1, len(string.ascii_lowercase)):
        loop_string.next_string()
    assert (loop_string.next_string() == 'aaz')

    for _ in range(1, len(string.ascii_lowercase)):
        loop_string.next_string()
    assert (loop_string.next_string() == 'abz')

    for _ in range(1, len(string.ascii_lowercase * len(string.ascii_lowercase))):
        loop_string.next_string()
    assert (loop_string.next_string() == 'bbz')


def test_brute_force_custom_chars():
    custom_string = BruteForceStringGenerator(chars='!@#', min_length=3)
    assert (custom_string.next_string() == '!!!')
    assert (custom_string.next_string() == '!!@')
    assert (custom_string.next_string() == '!!#')


def test_brute_force_brute_left():
    brute_string = BruteForceStringGenerator(dir=Direction.LEFT)
    for _ in range(1, 2000000):
        brute_string.next_string()

    assert (brute_string.next_string() == 'botid')


def test_brute_force_brute_right():
    brute_string = BruteForceStringGenerator()
    for _ in range(1, 2000000):
        brute_string.next_string()

    assert (brute_string.next_string() == 'ditob')


def test_brute_force_max_length():
    with pytest.raises(ValueError):
        brute_string = BruteForceStringGenerator('z', max_length=1)
        brute_string.next_string()
