def remove_punctuation(text: str) -> str:
    """Remove all punctuation from text, keeping letters and spaces.
    
    Example:
        >>> remove_punctuation("Hello, world!")
        "Hello world"
    """
    import string
    
    # Remove all punctuation characters
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Normalize whitespace (in case punctuation removal created extra spaces)
    return ' '.join(text.split())