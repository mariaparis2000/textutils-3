import textutils.core as c


def test_word_count_basic():
    """Test basic word counting with mixed case"""
    text = "Red red BLUE"
    assert c.word_count(text) == {"red": 2, "blue": 1}

def test_word_count_empty():
    """Test empty string returns empty dict"""
    assert c.word_count("") == {}

def test_word_count_single_word():
    """Test single word"""
    assert c.word_count("hello") == {"hello": 1}

def test_word_count_with_punctuation():
    """Test that punctuation is handled"""
    text = "Hello, world! Hello?"
    # This assumes we strip punctuation
    result = c.word_count(text)
    assert "hello" in result
    assert result["hello"] == 2
    

def test_normalize_whitespace_multiple_spaces():
    """Test collapsing multiple spaces"""
    text = "hello    world"
    assert c.normalize_whitespace(text) == "hello world"

def test_normalize_whitespace_leading_trailing():
    """Test removing leading and trailing spaces"""
    text = "   hello world   "
    assert c.normalize_whitespace(text) == "hello world"

def test_normalize_whitespace_newlines_tabs():
    """Test converting newlines and tabs to spaces"""
    text = "hello\n\tworld"
    assert c.normalize_whitespace(text) == "hello world"

def test_normalize_whitespace_complex():
    """Test complex whitespace scenario"""
    text = "  a   b \n  c  "
    assert c.normalize_whitespace(text) == "a b c"
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

def test_is_palindrome_not():
    """Test non-palindrome"""
    assert c.is_palindrome("hello") == False

def test_is_palindrome_basic():
    """Test basic palindrome"""
    assert c.is_palindrome("racecar") == True

def test_is_palindrome_with_spaces():
    """Test palindrome with spaces (should ignore)"""
    assert c.is_palindrome("race car") == True

def test_is_palindrome_case_insensitive():
    """Test that case is ignored"""
    assert c.is_palindrome("RaceCar") == True

def test_word_count_simple_merge():
    text = "hello,,world!!!"
    result = c.word_count(text)
    assert result == {"helloworld": 1}

def test_top_n_empty_dict():
    """Test top_n with empty dictionary (triggers 'if not counts:')"""
    assert c.top_n({}, 3) == []

def test_top_n_regular_dict():
    """Test top_n with a normal dictionary (triggers sorting and return)"""
    counts = {"apple": 2, "banana": 3, "cherry": 1}
    result = c.top_n(counts, 2)
    # Sorted by count descending, then alphabetically
    assert result == [("banana", 3), ("apple", 2)]

def test_top_n_n_greater_than_length():
    """Test top_n when n > number of items (triggers slicing return)"""
    counts = {"apple": 2, "banana": 3}
    result = c.top_n(counts, 5)
    assert result == [("banana", 3), ("apple", 2)]