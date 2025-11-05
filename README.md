# textutils
>
  ## Goals of the project

The goal of this project is to collaboratively build a small Python package called textutils while applying the development tools and workflows introduced in class — including Git, VS Code, micromamba, pytest, and coverage.
The main objective is to demonstrate effective teamwork through proper branching, merging, testing, and conflict resolution rather than creating a complex Python application.
>
## Project structure

textutils-3/
├── src/
│   └── textutils/
│       ├── __init__.py            # Package initialization
│       └── core.py                # Main feature implementations
│
├── tests/
│   ├── unit/
│   │   └── test_core.py           # Unit tests for individual functions
│   └── integration/
│       └── test_end_to_end.py     # Integration tests across features
│
├── environment.yml                # Environment setup for micromamba
├── pyproject.toml                 # Package configuration
└── README.md                      # Project documentation

## Installation
>
>1. Clone the repository:
>   ```bash
>   git clone https://github.com/mariaparis2000/textutils-3.git
>   cd textutils-3
>```
>
>
>2. Create the environment (with micromamba):
>
>   ```bash
>   micromamba create -f environment.yml -y
>   micromamba activate textutils
>   ```
>
>3. Install the package in editable mode:
>
>   ```bash
>   pip install -e .
>   ```
## Development Workflow

This project was developed collaboratively using *feature branches*, with each feature implemented and tested independently in tests/test_core.py. The workflow ensured that every new function was accompanied by corresponding unit tests.  

### Feature Branches and Implementations

- *feat/word-count*  
  - Implemented word_count(text) to count the frequency of words in a string (case-insensitive, ignores punctuation).  
  - Corresponding tests in test_core.py:  
    - test_word_count_basic – basic counting with mixed case  
    - test_word_count_empty – empty string  
    - test_word_count_single_word – single word  
    - test_word_count_with_punctuation – handles punctuation correctly

- *feat/normalize-whitespace*  
  - Implemented normalize_whitespace(text) to collapse multiple spaces, tabs, and newlines into single spaces, and remove leading/trailing spaces.  
  - Corresponding tests:  
    - test_normalize_whitespace_multiple_spaces  
    - test_normalize_whitespace_leading_trailing  
    - test_normalize_whitespace_newlines_tabs  
    - test_normalize_whitespace_complex

- *feat/remove-punctuation*  
  - Implemented remove_punctuation(text) to remove all punctuation from a string.  
  - Corresponding tests:  
    - test_remove_punctuation_basic  
    - test_remove_punctuation_multiple  
    - test_remove_punctuation_only_punct  
    - test_remove_punctuation_none

- *feat/is-palindrome*  
  - Implemented is_palindrome(text) to check if a string is a palindrome (ignores spaces and case).  
  - Corresponding tests:  
    - test_is_palindrome_not – non-palindrome  
    - test_is_palindrome_basic – basic palindrome  
    - test_is_palindrome_with_spaces – palindrome with spaces  
    - test_is_palindrome_case_insensitive – case-insensitive check

## Workflow Notes

1. Each feature was developed in its *own branch*.  
2. Unit tests for each feature were written in tests/test_core.py *before merging*, ensuring correctness.  
3. pytest and coverage reports (pytest --cov) were used to verify that all features worked as expected.  
4. After passing tests, each feature branch was merged into main, keeping the repository stable and testable at all times.  

This workflow promotes *test-driven development*, clear branch isolation, and easy collaboration between multiple developers.

## Running Tests
>
>To run all tests and check coverage:
>
>```bash
>pytest
>```
>
>To see detailed coverage information:
>
>```bash
>pytest --cov=src/textutils --cov-report=term-missing
>```
## Testing Coverage & Reliability

All features were tested using `pytest`, covering normal cases, edge cases, and type consistency.  
The final coverage report showed **100% test coverage** for all implemented functions.  
In addition to unit tests, integration tests in `tests/integration/test_end_to_end.py` verified the combined behavior of multiple functions (e.g., applying `remove_punctuation` and `word_count` sequentially).

## Summary of the Features
>
* `word_count(text)` → counts word frequencies (case-insensitive)
* `top_n(counts, n)` → returns the top-N frequent words
* `normalize_whitespace(text)` → collapses multiple spaces/newlines into one
* `remove_punctuation(text)` -> removes the punctuation
* `is_palindrome(text)`-> check if the text is a palindrome

## Feature Interactions

While each function can be used independently, they can also be combined to form simple text processing pipelines.  
For example:

```python
from textutils.core import remove_punctuation, normalize_whitespace, word_count

text = "Hello,   World!\nHello!"
cleaned = normalize_whitespace(remove_punctuation(text))
print(word_count(cleaned))
# {'hello': 2, 'world': 1}
```
## Team Members (Name, Institution, GitHub-Username)

- Fabrizio Iacuzio, ESADE (@FabrizioIacuzio)
- Maria Paris, ESADE (@mariaparis2000)
- Maximilian Voss, ESADE (@Maxv-svg)
- Baran Erdogan, ESADE (@baranerdogan11)
- Aumkar Wagle, ESADE (@awagle10)

## Final success criteria

- Git history shows that all team members contributed to the work
- Five features are included
- All tests passed at the end (`pytest -v`)
- README provides clear instructions
- Repository is easy to understand and cleaned up

## Important learnings

- Use a single source of communication (like WhatsApp)
- Run `pytest` after every change to not run into problems later
- Always `git pull` before `git push` to not have synchronisation problems
- Work together in the same room