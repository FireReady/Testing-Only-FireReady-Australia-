"""jeansdict: the Jeans Dictionary Tool, a small CLI dictionary/word tool."""

from .wordstat import (
    word_stats,
    count_syllables,
    count_vowels,
    count_consonants,
    is_palindrome,
    reverse_word,
)
from .anagrams import find_anagrams

__version__ = "0.1.0"

__all__ = [
    "word_stats",
    "count_syllables",
    "count_vowels",
    "count_consonants",
    "is_palindrome",
    "reverse_word",
    "find_anagrams",
]
