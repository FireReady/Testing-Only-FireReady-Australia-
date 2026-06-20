"""Tests for the anagrams module."""

import pytest

from jeansdict.anagrams import _signature, find_anagrams


@pytest.fixture
def wordlist(tmp_path):
    """Create a small, deterministic word list for testing."""
    words = ["listen", "silent", "enlist", "tinsel", "cat", "act", "dog", "hello"]
    path = tmp_path / "words.txt"
    path.write_text("\n".join(words) + "\n", encoding="utf-8")
    return path


def test_signature_matches_for_anagrams():
    assert _signature("listen") == _signature("silent")
    assert _signature("cat") == _signature("act")


def test_signature_differs_for_non_anagrams():
    assert _signature("cat") != _signature("dog")


def test_find_anagrams_excludes_self_by_default(wordlist):
    result = find_anagrams("listen", wordlist_path=wordlist)
    assert result == ["enlist", "silent", "tinsel"]
    assert "listen" not in result


def test_find_anagrams_include_self(wordlist):
    result = find_anagrams("listen", wordlist_path=wordlist, include_self=True)
    assert result == ["enlist", "listen", "silent", "tinsel"]


def test_find_anagrams_case_insensitive(wordlist):
    result = find_anagrams("LISTEN", wordlist_path=wordlist)
    assert result == ["enlist", "silent", "tinsel"]


def test_find_anagrams_none_found(wordlist):
    assert find_anagrams("zzzz", wordlist_path=wordlist) == []


def test_find_anagrams_empty_input(wordlist):
    assert find_anagrams("", wordlist_path=wordlist) == []


def test_find_anagrams_two_letter(wordlist):
    assert find_anagrams("cat", wordlist_path=wordlist) == ["act"]


def test_find_anagrams_against_bundled_list():
    """Smoke test against the real bundled word list."""
    result = find_anagrams("listen")
    assert "silent" in result
    assert "listen" not in result
