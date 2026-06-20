"""Tests for the wordstat module."""

import pytest

from worddict.wordstat import (
    count_consonants,
    count_syllables,
    count_vowels,
    is_palindrome,
    reverse_word,
    word_stats,
)


@pytest.mark.parametrize(
    "word,expected",
    [
        ("hello", "olleh"),
        ("a", "a"),
        ("", ""),
        ("Racecar", "racecaR"),
    ],
)
def test_reverse_word(word, expected):
    assert reverse_word(word) == expected


@pytest.mark.parametrize(
    "word,expected",
    [
        ("racecar", True),
        ("level", True),
        ("Racecar", True),  # case-insensitive
        ("A man a plan a canal Panama", True),  # ignores spaces/case
        ("hello", False),
        ("", False),  # empty is not a palindrome
        ("a", True),
    ],
)
def test_is_palindrome(word, expected):
    assert is_palindrome(word) is expected


@pytest.mark.parametrize(
    "word,expected",
    [
        ("hello", 2),
        ("aeiou", 5),
        ("AEIOU", 5),
        ("rhythm", 0),
        ("", 0),
    ],
)
def test_count_vowels(word, expected):
    assert count_vowels(word) == expected


@pytest.mark.parametrize(
    "word,expected",
    [
        ("hello", 3),
        ("aeiou", 0),
        ("rhythm", 6),
        ("", 0),
        ("hello!", 3),  # punctuation ignored
    ],
)
def test_count_consonants(word, expected):
    assert count_consonants(word) == expected


@pytest.mark.parametrize(
    "word,expected",
    [
        ("hello", 2),
        ("cat", 1),
        ("the", 1),
        ("make", 1),  # silent trailing e
        ("apple", 2),  # "le" ending kept
        ("banana", 3),
        ("", 0),
        ("queue", 1),
    ],
)
def test_count_syllables(word, expected):
    assert count_syllables(word) == expected


def test_word_stats_keys():
    stats = word_stats("hello")
    assert stats == {
        "word": "hello",
        "syllables": 2,
        "vowels": 2,
        "consonants": 3,
        "is_palindrome": False,
        "reversed": "olleh",
    }


def test_word_stats_palindrome():
    stats = word_stats("level")
    assert stats["is_palindrome"] is True
    assert stats["reversed"] == "level"
