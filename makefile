#! usr/bin/env bash

TEST_DIR=tests/

.PHONY: preInstall
preInstall:
	pip install --upgrade pip
	pip install -r requirements-dev.txt

.PHONY: createVirtualenv
createVirtualenv:
	python3 -m pip install --user virtualenv
	python3 -m venv env
	source env/bin/activate

.PHONY: test
test: cleanReport
	pytest $(TEST_DIR)


.PHONY: cleanReport
cleanReport:
	rm -rf .coverage


.PHONY: openReport
openReport: cleanReport
	coverage run --branch -m unittest discover --pattern 'test_*.py' --start-directory $(TEST_DIR)
	coverage report --show-missing --include vandor_rename.py
	coverage html --title 'Tests Coverage Report' --include vandor_rename.py
	open htmlcov/index.html

