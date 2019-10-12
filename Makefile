TEST_DIR=tests

help:
	@echo "    install"
	@echo "        Install dependencies"
	@echo "    create-env"
	@echo "        Create a virtualenv to the project"
	@echo "    format"
	@echo "        Apply black formatting to code."
	@echo "    lint"
	@echo "        Apply flake8 as linter and black for checking if code is formated"
	@echo "    test"
	@echo "        Run the tests"
	@echo "    open-report"
	@echo "        Open coverage report for tests at the browser"
	@echo "    clean"
	@echo "        Remove temporary files, cache and coverage things"

install:
	pip3 install --upgrade pip
	pip3 install -r requirements-dev.txt

create-env:
	python3 -m pip install --user virtualenv
	python3 -m venv env
	@echo 'Run: "source env/bin/activate"'

lint:
	black -t py37 -l 79 --check *.py $(TEST_DIR)
	flake8 *.py $(TEST_DIR)

format:
	black -t py37 -l 79 *.py $(TEST_DIR)

test: clean
	pytest --cov=vandor_rename --cov-report=html --verbose

clean:
	rm -rf .coverage htmlcov __pycache__ */__pycache__

open-report:
	pytest --cov=vandor_rename --cov-report=term-missing --cov-report=html
	xdg-open htmlcov/index.html || open htmlcov/index.html
