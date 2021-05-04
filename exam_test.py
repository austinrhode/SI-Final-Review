from exam import *

def test_convert_numbers_single():
    string = "9"
    expected = "nine"

    actual = convert_numbers(string)

    assert actual == expected

def test_convert_numbers_words():
    string = "High 5"
    expected = "High five"

    actual = convert_numbers(string)

    assert actual == expected


def test_convert_numbers_all():
    string = "1234567890"
    expected = "onetwothreefourfivesixseveneightninezero"

    actual = convert_numbers(string)

    assert actual == expected

def test_most_popular_word_simple():
    string = "test"
    expected = ("test", 1)

    actual = most_popular_word(string)

    assert actual == expected

def test_most_popular_word_case():
    string = "test Test"
    expected = ("test", 2)

    actual = most_popular_word(string)

    assert actual == expected

def test_most_popular_word_multiple_words():
    string = "Hello hello hello can anyone else here me"
    expected = ("hello", 3)

    actual = most_popular_word(string)

    assert actual == expected

def test_money_multiplier():
    n = 5
    amount = 100
    expected = 368.928

    actual = money_multiplier(amount, n)

    assert actual == expected


def test_remove_duplicates_average():
    list = [1, 1, 2, 3, 4, 4, 5]
    expected = [1, 2, 3, 4, 5]

    actual = remove_duplicates(list)

    assert actual == expected

def test_remove_duplicates_invalid():
    list = [1, 1, 2, 3, 4, 4, 5.5]

    try:
        remove_duplicates(list)
        assert False
    except AttributeError:
        assert True

def test_balanced():
    string = "()"
    
    expected = True
    actual = is_balanced(string)

    assert actual == expected

def test_balanced_multiple():
    string = "()()"
    
    expected = True
    actual = is_balanced(string)

    assert actual == expected

def test_balanced_embedded():
    string = "(())"
    
    expected = True
    actual = is_balanced(string)

    assert actual == expected

def test_not_balanced():
    string = "())"
    
    expected = False
    actual = is_balanced(string)

    assert actual == expected

def test_not_balanced_2():
    string = "()("
    
    expected = False
    actual = is_balanced(string)

    assert actual == expected

def test_not_balanced_embedded():
    string = "(()))"
    
    expected = False
    actual = is_balanced(string)

    assert actual == expected

def test_not_balanced_single_open():
    string = "("
    
    expected = False
    actual = is_balanced(string)

    assert actual == expected

def test_not_balanced_single_closed():
    string = ")"
    
    expected = False
    actual = is_balanced(string)

    assert actual == expected