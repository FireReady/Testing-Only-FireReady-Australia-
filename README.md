# Jeans Dictionary Tool

A small command-line dictionary / word tool written in Python. The CLI is
invoked as `jeans` and the importable package is `jeansdict`.

It provides two commands:

- **`wordstat <word>`** — syllable count, vowel/consonant counts, whether the
  word is a palindrome, and the word reversed.
- **`anagrams <word>`** — all anagrams of a word, found in a local English word
  list bundled with the package.

## Project layout

```
.
├── src/
│   └── jeansdict/
│       ├── __init__.py
│       ├── wordstat.py        # word statistics
│       ├── anagrams.py        # anagram finder
│       ├── cli.py             # command-line entry point
│       └── data/
│           └── words_alpha.txt  # bundled English word list (~370k words)
├── tests/
│   ├── test_wordstat.py
│   └── test_anagrams.py
├── Makefile
├── pyproject.toml
├── requirements.txt
└── README.md
```

The bundled word list is the public-domain
[`words_alpha.txt`](https://github.com/dwyl/english-words) list (~370,000
words). It is committed to the repository so the `anagrams` command works
offline with no extra setup.

## Installation

Requires Python 3.9+. The tool uses only the standard library at runtime.

```bash
# Install the package and the `jeans` CLI
make install

# Or, for development (editable install + test dependencies)
make install-dev
```

These wrap the equivalent `pip` commands (`pip install .` and
`pip install -e .` respectively), so you can also install with `pip` directly.

## Usage

After installing, use the `jeans` command:

### `wordstat`

```console
$ jeans wordstat hello
Word:        hello
Syllables:   2
Vowels:      2
Consonants:  3
Palindrome:  no
Reversed:    olleh

$ jeans wordstat racecar
Word:        racecar
Syllables:   3
Vowels:      3
Consonants:  4
Palindrome:  yes
Reversed:    racecar
```

### `anagrams`

```console
$ jeans anagrams listen
Anagrams of 'listen' (5 found):
  enlist
  inlets
  silent
  slinte
  tinsel

# Include the word itself in the results
$ jeans anagrams listen --include-self
```

### Running without installing

You can also run the CLI directly from the source tree:

```bash
PYTHONPATH=src python3 -m jeansdict.cli wordstat hello
```

## Library use

The functions are importable too:

```python
from jeansdict import word_stats, find_anagrams

word_stats("level")
# {'word': 'level', 'syllables': 2, 'vowels': 2,
#  'consonants': 3, 'is_palindrome': True, 'reversed': 'level'}

find_anagrams("cat")
# ['act', ...]
```

## Running the tests

```bash
make test
```

This runs the `pytest` suite in `tests/`, covering syllable/vowel/consonant
counting, palindrome detection, word reversal, and the anagram finder.

## Notes

- Syllable counting uses a common vowel-group heuristic (counting runs of
  vowels, treating `y` as a vowel, and dropping a silent trailing `e`). It is
  an estimate and may differ from a dictionary for irregular words.
- Anagram lookups exclude the queried word itself by default; pass
  `--include-self` to include it.
