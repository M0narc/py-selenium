install:
	pip install -r requirements.txt

test:
	pytest --html=reports/report.html

lint:
	flake8 pages tests
