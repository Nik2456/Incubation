

def palindrome(str):
    str_reverse = str[::-1]
    return str==str_reverse

def test_str_palindrome():
    assert palindrome("radar"), "String is not palindrome"

