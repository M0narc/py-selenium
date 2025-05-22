.PHONY: test test-headless test-ci lint format


install:
	pip install -r requirements.txt

test:
	pytest -s tests --browser=chrome

test-headless:
	pytest -s tests --browser=chrome --headless

test-ci:
	CI=true pytest -s tests --browser=chrome

lint:
	flake8 pages tests

format:
	isort .
