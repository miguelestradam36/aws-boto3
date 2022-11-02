##############################################################################################
# Variables
##############################################################################################

current_dir := $(realpath .)
SETUP_PATH = ${current_dir}\src\config\requirements.txt
APP_PATH = ${current_dir}\src\main.py
TEST_PATH = ${current_dir}\src\test\test_installments.py


##############################################################################################
# Single commands
##############################################################################################

.PHONY: awscript
awscript: ## Running main python scripts of the program
	@python ${APP_PATH}
	@echo FINISHED AWS SCRIPTS MAKE PROCESS
.PHONY: awscript
awscriptest: ## Running main python scripts of the program
	@pip install -r ${SETUP_PATH} --quiet
	@echo Packages installed...
.PHONY: awscript
awscriptinstall: ## Running main python scripts of the program
	@pytest ${TEST_PATH}
	@echo Test Process FINISHED

##############################################################################################
# Built-in command
##############################################################################################

.PHONY: build
build: awscript awscriptest awscriptinstall