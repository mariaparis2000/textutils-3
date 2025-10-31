import textutils.core as c

def test_remove_punctuation_basic():
    """Test basic punctuation removal"""
    text = "Hello, world!"
    assert c.remove_punctuation(text) == "Hello world"

def test_remove_punctuation_multiple():
    """Test multiple punctuation marks"""
    text = "What?! No way..."
    assert c.remove_punctuation(text) == "What No way"

def test_remove_punctuation_only_punct():
    """Test string with only punctuation"""
    text = "!!!"
    assert c.remove_punctuation(text) == ""

def test_remove_punctuation_none():
    """Test string with no punctuation"""
    text = "hello world"
    assert c.remove_punctuation(text) == "hello world"


def test_is_palindrome_basic():
    """Test basic palindrome"""
    assert c.is_palindrome("racecar") == True

def test_is_palindrome_with_spaces():
    """Test palindrome with spaces (should ignore)"""
    assert c.is_palindrome("race car") == True

def test_is_palindrome_case_insensitive():
    """Test that case is ignored"""
    assert c.is_palindrome("RaceCar") == True

def test_is_palindrome_not():
    """Test non-palindrome"""
    assert c.is_palindrome("hello") == False

def test_is_palindrome_empty():
    """Test empty string"""
    assert c.is_palindrome("") == True

def test_is_palindrome_single_char():
    """Test single character"""
    assert c.is_palindrome("a") == True