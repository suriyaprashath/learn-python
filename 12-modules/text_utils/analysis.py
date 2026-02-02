"""
Text Analysis Functions
Functions to analyze text and extract information.
"""

def count_words(text):
    """Count the number of words in text."""
    return len(text.split())

def count_vowels(text):
    """Count the number of vowels in text."""
    vowels = 'aeiouAEIOU'
    return sum(1 for char in text if char in vowels)

def word_frequency(text):
    """Return a dictionary of word frequencies."""
    words = text.lower().split()
    frequency = {}
    for word in words:
        # Remove punctuation
        word = word.strip('.,!?;:')
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

def count_characters(text, include_spaces=False):
    """Count characters in text."""
    if include_spaces:
        return len(text)
    return len(text.replace(" ", ""))

def find_longest_word(text):
    """Find the longest word in text."""
    words = text.split()
    return max(words, key=len) if words else ""
