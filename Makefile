TEST_DIR=tests/

install:
	pip3 install --upgrade pip
	pip3 install -r requirements-dev.txt

create-env:
	python3 -m pip install --user virtualenv
	python3 -m venv env

test: clean
	pytest $(TEST_DIR)

clean:
	rm -rf .coverage htmlcov __pycache__ */__pycache__

open-report: clean
	coverage run --branch -m unittest discover --pattern 'test_*.py' --start-directory $(TEST_DIR)
	coverage report --show-missing --include vandor_rename.py
	coverage html --title 'Tests Coverage Report' --include vandor_rename.py
	open htmlcov/index.html || xdg-open  htmlcov/index.html
