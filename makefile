##############################################################################################
# Variables
##############################################################################################

current_dir := $(realpath .)
SETUP_PATH = ${current_dir}\src\config\requirements.txt
APP_PATH = ${current_dir}\src\main.py
TEST_PATH = ${current_dir}\src\test\test_installments.py


.PHONY: awscript
awscript: ## Running main python scripts of the program
	@pip install -r {SETUP_PATH} --quiet
	@echo Packages installed...
	@pytest {TEST_PATH}
	@python {APP_PATH}