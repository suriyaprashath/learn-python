"""
Text Formatting Functions
Functions to format and transform text.
"""

def to_title_case(text):
    """Convert text to title case."""
    return text.title()

def reverse_text(text):
    """Reverse the text."""
    return text[::-1]

def remove_spaces(text):
    """Remove all spaces from text."""
    return text.replace(" ", "")

def add_padding(text, width=20, char=' '):
    """Add padding around text."""
    return text.center(width, char)

def truncate(text, max_length=50, suffix='...'):
    """Truncate text to maximum length."""
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix
