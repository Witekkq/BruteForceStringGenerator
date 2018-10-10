from brute_force_string_generator import BruteForceListGenerator


def test_brute_force_list_end():
    my_list = BruteForceListGenerator.create(sequence="aa", end='ad')
    assert (my_list == ['ab', 'ac', 'ad'])


def test_brute_force_list_num():
    my_list = BruteForceListGenerator.create(sequence="", num=2)
    assert (my_list == ['a', 'b'])
