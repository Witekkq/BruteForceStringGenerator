import string
from bruteforce import BruteForceStringGenerator


def test_brute_force_empty():
    default_init = BruteForceStringGenerator()
    assert (default_init.next_string() == 'a')


def test_brute_long_string():
    long_string = BruteForceStringGenerator(initial_sequence='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    assert (long_string.next_string() == 'baaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')


def test_brute_for_loop():
    loop_string = BruteForceStringGenerator(min_length=3)
    for i in range(1, len(string.ascii_lowercase)):
        loop_string.next_string()
    assert (loop_string.next_string() == 'zaa')

    for i in range(1, len(string.ascii_lowercase)):
        loop_string.next_string()
    assert (loop_string.next_string() == 'zba')

    for i in range(1, len(string.ascii_lowercase*len(string.ascii_lowercase))):
        loop_string.next_string()
    assert (loop_string.next_string() == 'zbb')


def test_brute_custom_chars():

    custom_string = BruteForceStringGenerator(chars='!@#', min_length=3)
    assert (custom_string.next_string() == '!!!')
    assert (custom_string.next_string() == '@!!')
    assert (custom_string.next_string() == '#!!')


def test_brute_brute():

    brute_string = BruteForceStringGenerator()
    for _ in range(1, 2000000):
        brute_string.next_string()
    assert (brute_string.next_string() == 'botid')
