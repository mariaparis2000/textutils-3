# textutils
>
> A small collaborative Python package that provides simple text utilities.
>
> ## Installation
>
>1. Clone the repository:
>   ```bash
>   git clone https://github.com/<owner>/textutils-<team>.git
>   cd textutils-<team>
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
>
>## Running Tests
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
>
>## Features
>
>* `word_count(text)` → counts word frequencies (case-insensitive)
>* `top_n(counts, n)` → returns the top-N frequent words
>* `normalize_whitespace(text)` → collapses multiple spaces/newlines into one
>
>## Team
>
>List the members of your group here with GitHub usernames.


<div class="alert alert-success">
