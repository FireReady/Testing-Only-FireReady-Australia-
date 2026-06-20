"""Find anagrams of a word using a local English word list."""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path

DEFAULT_WORDLIST = Path(__file__).parent / "data" / "words_alpha.txt"


def _signature(word: str) -> str:
    """Return a canonical signature for a word: its sorted lowercase letters."""
    return "".join(sorted(word.lower()))


@lru_cache(maxsize=4)
def _load_index(wordlist_path: str) -> dict[str, list[str]]:
    """Load the word list and index it by anagram signature.

    Results are cached so repeated lookups don't re-read the file.
    """
    index: dict[str, list[str]] = {}
    path = Path(wordlist_path)
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            word = line.strip().lower()
            if not word:
                continue
            index.setdefault(_signature(word), []).append(word)
    return index


def find_anagrams(
    word: str,
    wordlist_path: str | Path = DEFAULT_WORDLIST,
    include_self: bool = False,
) -> list[str]:
    """Return all words from the word list that are anagrams of ``word``.

    Args:
        word: The word to find anagrams for.
        wordlist_path: Path to the newline-delimited word list.
        include_self: If False (default), the word itself is excluded
            from the results.

    Returns:
        A sorted list of anagram words.
    """
    target = word.lower().strip()
    if not target:
        return []

    index = _load_index(str(wordlist_path))
    matches = index.get(_signature(target), [])

    if include_self:
        result = list(matches)
    else:
        result = [w for w in matches if w != target]

    return sorted(set(result))
