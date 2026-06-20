"""Command-line interface for worddict."""

from __future__ import annotations

import argparse
import sys

from .anagrams import find_anagrams
from .wordstat import word_stats


def _cmd_wordstat(args: argparse.Namespace) -> int:
    stats = word_stats(args.word)
    print(f"Word:        {stats['word']}")
    print(f"Syllables:   {stats['syllables']}")
    print(f"Vowels:      {stats['vowels']}")
    print(f"Consonants:  {stats['consonants']}")
    print(f"Palindrome:  {'yes' if stats['is_palindrome'] else 'no'}")
    print(f"Reversed:    {stats['reversed']}")
    return 0


def _cmd_anagrams(args: argparse.Namespace) -> int:
    anagrams = find_anagrams(args.word, include_self=args.include_self)
    if not anagrams:
        print(f"No anagrams found for '{args.word}'.")
        return 0
    print(f"Anagrams of '{args.word}' ({len(anagrams)} found):")
    for word in anagrams:
        print(f"  {word}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="worddict",
        description="A small CLI dictionary/word tool.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    stat_parser = subparsers.add_parser(
        "wordstat",
        help="Show syllable, vowel, consonant counts, palindrome status, and reversal.",
    )
    stat_parser.add_argument("word", help="The word to analyze.")
    stat_parser.set_defaults(func=_cmd_wordstat)

    ana_parser = subparsers.add_parser(
        "anagrams",
        help="Find anagrams of a word from the local word list.",
    )
    ana_parser.add_argument("word", help="The word to find anagrams for.")
    ana_parser.add_argument(
        "--include-self",
        action="store_true",
        help="Include the word itself in the results.",
    )
    ana_parser.set_defaults(func=_cmd_anagrams)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
