"""Word statistics: syllables, vowels, consonants, palindrome, reversal."""

from __future__ import annotations

VOWELS = frozenset("aeiou")


def reverse_word(word: str) -> str:
    """Return the word reversed."""
    return word[::-1]


def is_palindrome(word: str) -> bool:
    """Return True if the word reads the same forwards and backwards.

    Comparison is case-insensitive and ignores non-alphanumeric characters.
    An empty string is not considered a palindrome.
    """
    cleaned = [c for c in word.lower() if c.isalnum()]
    if not cleaned:
        return False
    return cleaned == cleaned[::-1]


def count_vowels(word: str) -> int:
    """Count the vowels (a, e, i, o, u) in the word, case-insensitively."""
    return sum(1 for c in word.lower() if c in VOWELS)


def count_consonants(word: str) -> int:
    """Count the consonants (alphabetic, non-vowel letters) in the word."""
    return sum(1 for c in word.lower() if c.isalpha() and c not in VOWELS)


def count_syllables(word: str) -> int:
    """Estimate the number of syllables in an English word.

    Uses a common heuristic: count groups of consecutive vowels (treating
    'y' as a vowel), subtract a trailing silent 'e', and ensure every word
    with letters has at least one syllable.
    """
    word = word.lower().strip()
    letters = [c for c in word if c.isalpha()]
    if not letters:
        return 0

    syllable_vowels = "aeiouy"
    count = 0
    prev_was_vowel = False
    for char in letters:
        is_vowel = char in syllable_vowels
        if is_vowel and not prev_was_vowel:
            count += 1
        prev_was_vowel = is_vowel

    # Silent trailing 'e' (e.g. "make", "cake") usually isn't a syllable,
    # but don't drop below one (e.g. "the", "she").
    if word.endswith("e") and not word.endswith(("le", "ee")) and count > 1:
        count -= 1

    return max(count, 1)


def word_stats(word: str) -> dict:
    """Return a dictionary of statistics for the given word."""
    return {
        "word": word,
        "syllables": count_syllables(word),
        "vowels": count_vowels(word),
        "consonants": count_consonants(word),
        "is_palindrome": is_palindrome(word),
        "reversed": reverse_word(word),
    }
