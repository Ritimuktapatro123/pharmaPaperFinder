# pharma-paper-finder

A command-line tool to fetch research papers from PubMed based on a user-defined query and filter out papers authored by individuals affiliated with pharmaceutical or biotech companies.


## Project Structure

```
pharma-paper-finder/
├── pyproject.toml
├── README.md
├── src/
│   └── pharma_paper_finder/
│       ├── __init__.py
│       ├── api.py              # Handles PubMed API queries and response parsing
│       ├── filters.py          # Functions to detect and filter out non-academic authors
│       ├── writer.py           # Writes filtered data to a CSV file
│       └── cli.py              # CLI logic using argparse
├── tests/
│   └── test_fetcher.py         # Unit tests for filters and logic

```

## 🧰 Tools & Libraries Used

- [`Poetry`](https://python-poetry.org/) for dependency and package management.
- [`requests`](https://pypi.org/project/requests/) for making PubMed API calls.
- [`xml.etree.ElementTree`](https://docs.python.org/3/library/xml.etree.elementtree.html) for parsing XML.
- [`argparse`](https://docs.python.org/3/library/argparse.html) for building CLI.
- [`pytest`](https://docs.pytest.org/) for unit testing.
- **PubMed API**: [https://eutils.ncbi.nlm.nih.gov/entrez/eutils/](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/)


## ⚙️ Installation & Usage
---
### 1.Clone the repository

- [git clone https://github.com/your-username/pharma-paper-finder.git](https://github.com/Ritimuktapatro123/pharmaPaperFinder.git)
- cd pharma-paper-finder

### 2. Install using Poetry
- Make sure Poetry is installed. 
- Then:
- poetry install

### 3.Activate the virtual environment
- poetry shell

### 4. Run the CLI tool
- get-papers-list -q "cancer immunotherapy" -d 2023 -f output.csv

- Use --help to view available options:
- get-papers-list --help

### 5.Running Tests
- Run all unit tests using:
- poetry run pytest

### 6.Publishing to TestPyPI
- To publish your module to TestPyPI:
- Build and publish:
- poetry publish -r test-pypi --build
- Check your package:

- Visit:
- https://test.pypi.org/project/pharma-paper-finder/
- You’ll see your version, files, and metadata if successfully published.

- Install from TestPyPI:
- pip install -i https://test.pypi.org/simple/ pharma-paper-finder

## Author
- Ritimukta Patro
- Computer Science Graduate
- Built using Python, Poetry, and Open Source tools

---
