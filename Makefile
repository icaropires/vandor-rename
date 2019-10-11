TEST_DIR=tests

install:
	pip3 install --upgrade pip
	pip3 install -r requirements-dev.txt

create-env:
	python3 -m pip install --user virtualenv
	python3 -m venv env
	@echo 'Run: "source env/bin/activate"'

test: clean
	pytest --cov=vandor_rename --cov-report=html

clean:
	rm -rf .coverage htmlcov __pycache__ */__pycache__

open-report:
	pytest --cov=vandor_rename --cov-report=term-missing --cov-report=html
	open htmlcov/index.html
	open htmlcov/index.html || xdg-open htmlcov/index.html
