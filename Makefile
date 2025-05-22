.PHONY: test test-headless test-ci lint format


install:
	pip install -r requirements.txt

test:
	pytest -s tests --browser=chrome

test-headless:
	pytest -s tests --browser=chrome --headless

test-ci:
	CI=true pytest -s tests --browser=
	
test-allure:
	pytest --alluredir=reports/allure-results

report:
	allure generate reports/allure-results -o reports/allure-report --clean

open-report:
	allure open reports/allure-report

lint:
	flake8 pages tests

format:
	isort .
