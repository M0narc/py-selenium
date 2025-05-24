.PHONY: test test-headless test-ci lint format test-dc dc-report dc-open build install test-allure report open-report

# ==== Comandos locales ==== #

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

# ==== Comandos Docker ==== #

build:
	docker-compose build

test-dc:
	docker-compose run --rm tests pytest -s tests --browser=chrome --headless --alluredir=reports/allure-results

dc-report:
	docker-compose run --rm tests allure generate reports/allure-results -o reports/allure-report --clean

dc-open:
	docker-compose run --rm tests allure open reports/allure-report
