import string
import pytest

from brute_force_string_generator import BruteForceStringGenerator, Direction


def test_brute_force_empty():
    default_init = BruteForceStringGenerator()
    assert (next(default_init) == 'a')


def test_brute_force_direction():
    direction_test = BruteForceStringGenerator(sequence='aa', direction=Direction.LEFT)
    assert (next(direction_test) == 'ba')
    direction_test = BruteForceStringGenerator(sequence='aa', direction=Direction.RIGHT)
    assert (next(direction_test) == 'ab')


def test_brute_force_edge():
    direction_test = BruteForceStringGenerator(sequence='za', direction=Direction.LEFT)
    assert (next(direction_test) == 'ab')
    direction_test = BruteForceStringGenerator(sequence='az', direction=Direction.RIGHT)
    assert (next(direction_test) == 'ba')


def test_brute_force_long_string():
    long_string = BruteForceStringGenerator(sequence='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    assert (next(long_string) == 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab')


def test_brute_force_for_loop():
    loop_string = BruteForceStringGenerator(min_length=3)
    for _ in range(1, len(string.ascii_lowercase)):
        next(loop_string)
    assert (next(loop_string) == 'aaz')

    for _ in range(1, len(string.ascii_lowercase)):
        next(loop_string)
    assert (next(loop_string) == 'abz')

    for _ in range(1, len(string.ascii_lowercase * len(string.ascii_lowercase))):
        next(loop_string)
    assert (next(loop_string) == 'bbz')


def test_brute_force_custom_chars():
    custom_string = BruteForceStringGenerator(chars='!@#', min_length=3)
    assert (next(custom_string) == '!!!')
    assert (next(custom_string) == '!!@')
    assert (next(custom_string) == '!!#')


def test_brute_force_brute_left():
    brute_string = BruteForceStringGenerator(direction=Direction.LEFT)
    for _ in range(1, 2000000):
        next(brute_string)
    assert (next(brute_string) == 'botid')


def test_brute_force_brute_right():
    brute_string = BruteForceStringGenerator()
    for _ in range(1, 2000000):
        next(brute_string)
    assert (next(brute_string) == 'ditob')


def test_brute_force_max_length():
    with pytest.raises(StopIteration):
        brute_string = BruteForceStringGenerator('z', max_length=1)
        next(brute_string)


def test_brute_force_generator():
    brute_string = BruteForceStringGenerator(max_length=3)
    for text in brute_string:
        pass
    assert (text == 'zzz')


def test_not_direction_type():
    for i in range(-1, 2):
        with pytest.raises(ValueError):
            BruteForceStringGenerator('a', max_length=1, direction=i)

