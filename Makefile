.PHONY: help install install-dev test clean

PYTHON ?= python3

help:
	@echo "Available targets:"
	@echo "  make install      Install the worddict package (and CLI)"
	@echo "  make install-dev  Install in editable mode with test deps"
	@echo "  make test         Run the pytest test suite"
	@echo "  make clean        Remove build artifacts and caches"

install:
	$(PYTHON) -m pip install .

install-dev:
	$(PYTHON) -m pip install -e .
	$(PYTHON) -m pip install -r requirements.txt

test:
	$(PYTHON) -m pytest

clean:
	rm -rf build dist *.egg-info src/*.egg-info .pytest_cache
	find . -type d -name __pycache__ -exec rm -rf {} +
