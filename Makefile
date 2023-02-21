.PHONY: install format lint test sec

install:
	@poetry install
format:
	@black -l 88 .
lint:
	@black . --check
	@pylint src
	@pylint tests
test:
	@pytest --cov=src tests/
sec:
	@pip-audit