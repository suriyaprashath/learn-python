# Text Utils Package
# This file makes the 'text_utils' folder a Python package

from .formatting import to_title_case, reverse_text, remove_spaces
from .analysis import count_words, count_vowels, word_frequency

__all__ = [
    'to_title_case', 'reverse_text', 'remove_spaces',
    'count_words', 'count_vowels', 'word_frequency'
]
