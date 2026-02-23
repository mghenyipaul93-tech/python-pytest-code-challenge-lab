import pytest
from lib.palindrome import longest_palindromic_substring

@pytest.mark.parametrize("input_str, expected", [
    ("babad", ["bab", "aba"]),
    ("cbbd", ["bb"]),
    ("racecar", ["racecar"]),
])
def test_normal_cases(input_str, expected):
    result = longest_palindromic_substring(input_str)
    assert result in expected

def test_single_character():
    assert longest_palindromic_substring("a") == "a"


def test_two_diff_characters():
    result = longest_palindromic_substring("ac")
    assert result in ["a", "c"]


def test_full_palindrome():
    assert longest_palindromic_substring("madam") == "madam"


def test_numeric_string():
    assert longest_palindromic_substring("12321") == "12321"


def test_long_string():
    input_str = "forgeeksskeegfor"
    assert longest_palindromic_substring(input_str) == "geeksskeeg"


def test_empty_string():
    assert longest_palindromic_substring("") == ""


def test_invalid_input():
    with pytest.raises(TypeError):
        longest_palindromic_substring(123)