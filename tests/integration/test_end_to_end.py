import textutils.core as c

def test_word_analysis_pipeline():
    text = "Hello, world! Hello Python. Python is great!"
    cleaned = c.remove_punctuation(text)
    counts = c.word_count(cleaned)
    top_words = c.top_n(counts, 2)
    assert ("hello", 2) in top_words or ("python", 2) in top_words
    
def test_palindrome_with_normalization():
    text = "  race   car  "
    normalized = c.normalize_whitespace(text)
    assert c.is_palindrome(normalized) == True